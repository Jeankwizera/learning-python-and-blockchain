
blockchain = ["block 1"]
block = ["trans 1"]
invoices = [0]

sender = ["jeanK", 1000]
recepient = ["MeApp", 97]

def transact(invoices):
    
    receipt = []
    invoice_number = invoices[-1] + 1
    invoices.append(invoice_number)
    receipt.append(invoice_number)
        
    sender_address = sender[0]
    receipt.append(sender_address)
        
    sender_balance = sender[-1]
        
    amount = float(input("Enter Amount To Send: "))
    receipt.append(amount)
        
    new_sender_balance = sender_balance - amount
    sender.append(new_sender_balance)
        
    recepient_address = recepient[0]
    receipt.append(recepient_address)
        
    recepient_balance = recepient[-1]
    new_recepient_balance = recepient_balance + amount
    recepient.append(new_recepient_balance)
        
    purpose = input("Enter Reason For Payment: ")
    receipt.append(purpose)
    
    print(receipt)
    comment()
    
    block.append(receipt)
    
def hashing(block):
    block = print(block)
    block_hash = hash(block)
    return(block_hash)

def comment():
    comm = input("Satisfied?: ")
    block.append(comm)
    
def get_last_block(blockchain):
        return(blockchain[-1])
   
def add_block_to_blockchain():
    last_block = get_last_block(blockchain)
    print("Block Full")
    
    block_hash = hashing(block)
    
    print("Adding Block to Blockchain")
    blockchain.append([last_block, block_hash])
    print(blockchain)
    send_money()    
                    
def transactions():
    
    transact(invoices)
    print(sender)
    print(recepient)
    
    transact(invoices)
    print(sender)
    print(recepient)

    transact(invoices)
    print(sender)
    print(recepient)
    
    
    
def send_money():
    transactions()
    add_block_to_blockchain()

send_money()
    
    
        

    
    
    
       