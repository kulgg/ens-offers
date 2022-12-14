from opensea import OpenseaAPI
from datetime import datetime, timezone
from opensea import utils as opensea_utils

def main():
    api = OpenseaAPI(apikey="YOUR APIKEY")

    contract_address = "0x495f947276749Ce646f68AC8c248420045cb7b5e"
    token_id = "66406747123743156841746366950152533278033835913591691491127082341586364792833"

    result = api.asset(asset_contract_address=contract_address, token_id=token_id)
    print(result)
    # result = api.assets(owner="0xce90a7949bb78892f159f428d0dc23a8e3584d75", limit=3)
    # result = api.contract(asset_contract_address="0x495f947276749Ce646f68AC8c248420045cb7b5e")
    # result = api.collection(collection_slug="cryptopunks")
    # result = api.collections(asset_owner="0xce90a7949bb78892f159f428d0dc23a8e3584d75", limit=3)
    # result = api.collection_stats(collection_slug="cryptopunks")

    # period_end = opensea_utils.datetime_utc(2021, 11, 6, 14, 30)
    # result = api.events(
    #     occurred_before=period_end,
    #     limit=10,
    #     export_file_name="events.json",
    # )
    # result = api.bundles(limit=2)


    # start_at = datetime(2021, 10, 5, 3, 25, tzinfo=timezone.utc)
    # finish_at = datetime(2021, 10, 5, 3, 20, tzinfo=timezone.utc)

    # event_generator = api.events_backfill(start=start_at,
    #                                       until=finish_at,
    #                                       event_type="successful")
    # for event in event_generator:
    #     if event is not None:
    #         print(event) # or do other things with the event data
    
if __name__ == '__main__':
    main()