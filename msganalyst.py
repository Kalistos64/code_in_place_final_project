import sys
import datetime

def main():
#open a whatsapp log text file
    if len(sys.argv) < 2:
        print("Usage: python msganalyst.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    f = open(filename,"r", encoding='latin-1')

#splits the text in stripped lines
    total_messages = splitlines(f)

#converts the text into a dictionary where each value is a date and each key is a list of tuple corresponding to each message's hour, sender and content info
    total_messages_infoformat = extractinfo(total_messages)
    print(total_messages_infoformat)

#create a sender count variable where each key is the name of a sender and each value how many times he was the conversation starter
    senders = {}

#access the first value of each key of the totalmessageinfoformat dictionnary, which is the first message of a given day, formatted
    for day, message in total_messages_infoformat.items():
        first_message = message[0]
    #access the sender info and make the sender's count go up by one each time
        sender = first_message[1]
        if sender not in senders:
            senders.update({sender:1})
        else:
            senders[sender] +=1

    #prints how many times each person started a conversation on a new day
    for sender, count in senders.items():
        print(f"{sender} has started the conversation {count} times")
  


#split a text in lines corresponding to each message on a whatsapp log and remove the weird buggy character
def splitlines(file):
    total_lines = []
    for line in file:
        line = line.replace("â\x80¯"," ")
        total_lines.append(line.strip())
    return total_lines


# returns the messages in a dictionary format where each key is a date and
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