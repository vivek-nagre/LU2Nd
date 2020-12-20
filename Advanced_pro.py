import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("myfirebasekey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'vivek',
#     u'last': u'nagre',
#     u'born': 1998
# })

def EnterDataBqse():
    doc_ref = db.collection(u'MyBro').document()
    dit={}
    name=input("enter your name:")
    lastname=input("enter your Lastname:")
    age=int(input("enter your age:"))
    dit["first"]=name
    dit["last"]=lastname
    dit["born"]=age

    doc_ref.set(dit)

docs = db.collection(u'MyBro').stream()
print("..............i have the folloing datatset along with me.............")
for doc in docs:
    # print(f"{doc.id} => {doc.to_dict()}")
    print("ID-",doc.id)
    print("First name -",doc.to_dict().get("first"))
    print("last name -",doc.to_dict().get("last"))
    print("age -",doc.to_dict().get("born"))
    print("-"*50)
    print("-"*50)
# EnterDataBqse()   
def updateDatabase(uid,upadateAge):
    doc_ref = db.collection(u'MyBro').document(uid)
    doc_ref.set({"age":upadateAge})
updateDatabase("rzorPfEDnbJPDKeslXgg",23)
