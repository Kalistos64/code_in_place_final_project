import sys
import datetime

def main():
#open a whatsapp log text file
    if len(sys.argv) < 2:
        print("Usage: python msganalyst.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    f = open(filename,"r", encoding='latin-1')

#split the text in stripped lines
    total_messages = splitlines(f)

#converts the text into a dictionary where each value is a date and each key is a tuple of corresponding info
    total_messages_infoformat = extractinfo(total_messages)
#create a sender count variable
    senders = {}

#access the first value of each key of the dictionnary
    for day, message in total_messages_infoformat.items():
        first_message = message[0]
    #access the sender info and make the sender's count go up by one each time
        sender = first_message[1]
        if sender not in senders:
            senders.update({sender:1})
        else:
            senders[sender] +=1
    
    for sender, count in senders.items():
        print(f"{sender} has started the conversation {count} times")
  


#split a text in lines corresponding to each message on a whatsapp log and remove the weird buggy character
def splitlines(file):
    total_lines = []
    for line in file:
        line = line.replace("â\x80¯"," ")
        total_lines.append(line.strip())
    return total_lines

def extractinfo(stripped_text):
    infoformat_text ={}
    for line in stripped_text:
        if not line.strip(): 
            continue
        try:
            line = line.split(",", 1)
            date = line[0].strip()
            line = line[1].split("-", 1)
            time = line[0].strip()
            line = line[1].split(":", 1)
            sender = line[0].strip()
            content = line[1].strip()
        except (IndexError, ValueError):
            continue

        if date not in infoformat_text:
            infoformat_text[date] = [(time,sender,content)]
        
        else:
            infoformat_text[date].append((time,sender,content))
    return infoformat_text



if __name__ == "__main__":
    main()