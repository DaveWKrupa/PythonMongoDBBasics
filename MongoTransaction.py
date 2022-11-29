import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

client = MongoClient(MONGODB_URI)

def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None
):

    accounts_collection = session.client.bank.accounts

    transfer_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfer_complete": transfer_id},
        },
        session=session,
    )

    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfer_complete": transfer_id},
        },
        session=session,
    )

    transfer_collection.insert_one(transfer, session=session)
    print("Transfer successful")
    return

def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR29384672398",
        account_id_receiver="MDB9236y432",
        account_id_sender="MDB239487",
        transfer_amount=100,
    )

with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()