
blockchain = ["block 1"]
block = ["trans 1"]
invoices = [0]

def send_money( ):   
    
    amount = float(input("Enter Amount To Send: "))
    sender_email = input("Enter Sender Email: ")
    recepient_email = input("Enter Recepient Email: ")
    
    purpose = input("Enter Reason For Payment: ")

    sender_balance = [100]
    recepient_balance = [100]
    
    new_sender_balance = sender_balance[-1] - amount
    sender_balance.append(new_sender_balance)
    
    new_recepient_balance = recepient_balance[-1] + amount
    recepient_balance.append(new_recepient_balance)
    
    invoice_number = invoices[-1] + 1
    invoices.append(invoice_number)
    
    transaction = print(["using", invoice_number, sender_email, 
                       "sends", amount, "remains", 
                       sender_balance[-1], "to", recepient_email,
                       "becomes", recepient_balance[-1], "for",
                       purpose])
    return(transaction)

def add_transaction_to_block( ):
    transaction = send_money( )
    block.append(transaction)
    return(block)

def get_last_block( ):
    last_block = blockchain[-1]
    return(last_block)
    
def transact( ):
    block = add_transaction_to_block( )
    blockchain.append([get_last_block( ), block])
    return(blockchain)
    
    print(add_transaction_to_block( ))
    print(blockchain)
    
    
    
    
       