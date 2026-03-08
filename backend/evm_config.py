#!/usr/bin/env python3
"""
Injective EVM Configuration

Provides network configuration for Injective's EVM compatibility layer.
Supports both mainnet and testnet chains.
"""

# Injective EVM Mainnet Configuration
# Cosmos chain-id: injective-1  |  EVM chain-id: 1776
INJECTIVE_EVM_MAINNET = {
    "chainId": 1776,
    "chainName": "Injective",
    "chainHex": "0x6f0",
    "rpcUrl": "https://sentry.evm-rpc.injective.network/",
    "wsUrl": "wss://sentry.evm-ws.injective.network",
    "blockExplorerUrl": "https://blockscout.injective.network/",
    "blockExplorerApiUrl": "https://blockscout-api.injective.network/api",
    "nativeCurrency": {
        "name": "Injective",
        "symbol": "INJ",
        "decimals": 18
    },
    "description": "Injective EVM Mainnet",
    "contracts": {
        "USDT": "0x88f7F2b685F9692caf8c478f5BADF09eE9B1Cc13",
        "wETH": "0x83A15000b753AC0EeE06D2Cb41a69e76D0D5c7F7",
        "wINJ": "0x0000000088827d2d103ee2d9A6b781773AE03FfB",
        "USDC": "0x2a25fbD67b3aE485e461fe55d9DbeF302B7D3989",
        "MultiCall": "0xcA11bde05977b3631167028862bE2a173976CA11"
    }
}

# Injective EVM Testnet Configuration
# Cosmos chain-id: injective-888  |  EVM chain-id: 1439
INJECTIVE_EVM_TESTNET = {
    "chainId": 1439,
    "chainName": "Injective Testnet",
    "chainHex": "0x59f",
    "rpcUrl": "https://k8s.testnet.json-rpc.injective.network/",
    "wsUrl": "wss://k8s.testnet.ws.injective.network/",
    "blockExplorerUrl": "https://testnet.blockscout.injective.network/",
    "blockExplorerApiUrl": "https://testnet.blockscout-api.injective.network/api",
    "faucetUrl": "https://testnet.faucet.injective.network/",
    "nativeCurrency": {
        "name": "Injective Testnet",
        "symbol": "INJ",
        "decimals": 18
    },
    "description": "Injective EVM Testnet - For testing and development",
    "contracts": {
        "wINJ": "0x0000000088827d2d103ee2d9A6b781773AE03FfB",
        "USDT": "0xaDC7bcB5d8fe053Ef19b4E0C861c262Af6e0db60"
    }
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
