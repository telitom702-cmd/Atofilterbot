import pymongo
from config import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME

class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(DATABASE_URI)
        self.db = self.client[DATABASE_NAME]
        self.col = self.db[COLLECTION_NAME]

    def save_file(self, file_id, file_name, file_size, caption, chat_id, message_id):
        """
        Upsert মেথড: আগে থেকে ফাইল থাকলে আপডেট করবে, না থাকলে নতুন করে অ্যাড করবে।
        এতে ডাটাবেস কনফ্লিক্ট বা ডুপ্লিকেট হবে না।
        """
        filter_query = {
            "file_id": file_id,
            "chat_id": chat_id
        }
        update_query = {
            "$set": {
                "file_name": file_name,
                "file_size": file_size,
                "caption": caption,
                "message_id": message_id
            }
        }
        # upsert=True হলে ডাটা না পেলে ইনসার্ট করে, পেলে আপডেট করে
        self.col.update_one(filter_query, update_query, upsert=True)

    def get_search_results(self, query, file_type=None, max_results=10):
        query = query.replace(" ", r".*")
        filter_query = {"file_name": {"$regex": query, "$options": "i"}}
        if file_type:
            filter_query["file_type"] = file_type
            
        cursor = self.col.find(filter_query).limit(max_results)
        return list(cursor)

# Initialize DB
db = Database()
