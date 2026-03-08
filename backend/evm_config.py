#!/usr/bin/env python3
"""
Injective EVM Configuration

Provides network configuration for Injective's EVM compatibility layer.
Supports both mainnet and testnet chains.
"""

# Injective EVM Mainnet Configuration
INJECTIVE_EVM_MAINNET = {
    "chainId": 60,
    "chainName": "Injective",
    "chainHex": "0x3c",
    "rpcUrl": "https://evm.injective.network",
    "blockExplorerUrl": "https://explorer.injective.network",
    "nativeCurrency": {
        "name": "Injective",
        "symbol": "INJ",
        "decimals": 18
    },
    "description": "Injective EVM Mainnet - The fastest and most liquid decentralized derivatives exchange"
}

# Injective EVM Testnet Configuration
INJECTIVE_EVM_TESTNET = {
    "chainId": 888,
    "chainName": "Injective Testnet",
    "chainHex": "0x378",
    "rpcUrl": "https://evm.testnet.injective.network",
    "blockExplorerUrl": "https://testnet.explorer.injective.network",
    "nativeCurrency": {
        "name": "Injective Testnet",
        "symbol": "INJ",
        "decimals": 18
    },
    "description": "Injective EVM Testnet - For testing and development"
}

# Network registry
NETWORKS = {
    "mainnet": INJECTIVE_EVM_MAINNET,
    "testnet": INJECTIVE_EVM_TESTNET,
}

def get_network(network_name: str):
    """Get network configuration by name."""
    return NETWORKS.get(network_name.lower(), INJECTIVE_EVM_MAINNET)

def get_all_networks():
    """Get all available networks."""
    return NETWORKS

def get_rpc_url(network_name: str):
    """Get RPC URL for a network."""
    network = get_network(network_name)
    return network.get("rpcUrl")

def get_chain_id(network_name: str):
    """Get chain ID for a network."""
    network = get_network(network_name)
    return network.get("chainId")

def format_chain_id_hex(chain_id: int):
    """Convert chain ID to hex format for MetaMask."""
    return f"0x{chain_id:x}"
