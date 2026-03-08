#!/usr/bin/env python3
"""
Viem-based EVM Wallet Utilities for Injective

Provides:
- MetaMask provider detection and interaction
- Balance queries via viem/ethers.js
- Network switching support
- Transaction signing (delegated to frontend)
"""

import os
import json
import requests
from typing import Optional, Dict, Any
from evm_config import get_network, get_all_networks


class ViemWalletManager:
    """Manages EVM wallet operations with viem/MetaMask."""

    def __init__(self):
        self.session = requests.Session()
        self.session.timeout = 10
        # Disable SSL verification for development (RPC endpoints may have SSL issues)
        # In production, use proper certificates
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.session.verify = False

    def get_networks(self) -> Dict[str, Any]:
        """Get all available networks."""
        return get_all_networks()

    def get_network_info(self, network: str) -> Dict[str, Any]:
        """Get specific network configuration."""
        net = get_network(network)
        return {
            "ok": True,
            "network": network,
            "config": net
        }

    def get_balance(self, address: str, network: str = "mainnet") -> Dict[str, Any]:
        """Query balance for an address using JSON-RPC."""
        try:
            if not address.startswith("0x"):
                return {"ok": False, "error": "Invalid address format (must start with 0x)"}

            net = get_network(network)
            rpc_url = net.get("rpcUrl")

            if not rpc_url:
                return {"ok": False, "error": f"RPC URL not configured for {network}"}

            # JSON-RPC call: eth_getBalance
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_getBalance",
                "params": [address, "latest"],
                "id": 1
            }

            response = self.session.post(rpc_url, json=payload)
            
            if response.status_code != 200:
                return {"ok": False, "error": f"RPC request failed: {response.status_code}"}

            result = response.json()

            if "error" in result:
                return {"ok": False, "error": result["error"].get("message", "RPC error")}

            balance_hex = result.get("result", "0x0")
            balance_wei = int(balance_hex, 16)
            balance_inj = balance_wei / 1e18

            return {
                "ok": True,
                "address": address,
                "network": network,
                "balance": {
                    "wei": str(balance_wei),
                    "inj": f"{balance_inj:.6f}",
                    "human": f"{balance_inj:.6f} INJ"
                }
            }

        except Exception as e:
            return {"ok": False, "error": str(e)}

    def get_gas_price(self, network: str = "mainnet") -> Dict[str, Any]:
        """Get current gas price."""
        try:
            net = get_network(network)
            rpc_url = net.get("rpcUrl")

            if not rpc_url:
                return {"ok": False, "error": f"RPC URL not configured for {network}"}

            # JSON-RPC call: eth_gasPrice
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_gasPrice",
                "params": [],
                "id": 1
            }

            response = self.session.post(rpc_url, json=payload)
            
            if response.status_code != 200:
                return {"ok": False, "error": f"RPC request failed: {response.status_code}"}

            result = response.json()

            if "error" in result:
                return {"ok": False, "error": result["error"].get("message", "RPC error")}

            gas_price_hex = result.get("result", "0x0")
            gas_price_wei = int(gas_price_hex, 16)
            gas_price_gwei = gas_price_wei / 1e9

            return {
                "ok": True,
                "network": network,
                "gasPrice": {
                    "wei": str(gas_price_wei),
                    "gwei": f"{gas_price_gwei:.2f}",
                    "human": f"{gas_price_gwei:.2f} Gwei"
                }
            }

        except Exception as e:
            return {"ok": False, "error": str(e)}

    def get_block_number(self, network: str = "mainnet") -> Dict[str, Any]:
        """Get current block number."""
        try:
            net = get_network(network)
            rpc_url = net.get("rpcUrl")

            if not rpc_url:
                return {"ok": False, "error": f"RPC URL not configured for {network}"}

            # JSON-RPC call: eth_blockNumber
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_blockNumber",
                "params": [],
                "id": 1
            }

            response = self.session.post(rpc_url, json=payload)
            
            if response.status_code != 200:
                return {"ok": False, "error": f"RPC request failed: {response.status_code}"}

            result = response.json()

            if "error" in result:
                return {"ok": False, "error": result["error"].get("message", "RPC error")}

            block_hex = result.get("result", "0x0")
            block_num = int(block_hex, 16)

            return {
                "ok": True,
                "network": network,
                "blockNumber": block_num
            }

        except Exception as e:
            return {"ok": False, "error": str(e)}

    def estimate_gas(self, tx: Dict[str, Any], network: str = "mainnet") -> Dict[str, Any]:
        """Estimate gas for a transaction."""
        try:
            net = get_network(network)
            rpc_url = net.get("rpcUrl")

            if not rpc_url:
                return {"ok": False, "error": f"RPC URL not configured for {network}"}

            # JSON-RPC call: eth_estimateGas
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_estimateGas",
                "params": [tx],
                "id": 1
            }

            response = self.session.post(rpc_url, json=payload)
            
            if response.status_code != 200:
                return {"ok": False, "error": f"RPC request failed: {response.status_code}"}

            result = response.json()

            if "error" in result:
                return {"ok": False, "error": result["error"].get("message", "RPC error")}

            gas_hex = result.get("result", "0x0")
            gas_estimate = int(gas_hex, 16)

            return {
                "ok": True,
                "network": network,
                "gasEstimate": gas_estimate
            }

        except Exception as e:
            return {"ok": False, "error": str(e)}


# Global instance
wallet_manager = ViemWalletManager()
