from zksync2.module.module_builder import ZkSyncBuilder
RPC_ZKSYNC="https://zksync-era.blockpi.network/v1/rpc/public"

web3 = ZkSyncBuilder.build(RPC_ZKSYNC)
if __name__ == "__main__":
    print("hello",web3)