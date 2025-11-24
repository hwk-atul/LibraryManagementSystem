from datetime import datetime, timedelta
def addbook():
    bid = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    qty = input("Enter Quantity: ")
    try:
        f = open("library.txt", "a")
        f.write(bid + "," + title + "," + author + "," + qty + "\n")
        f.close()
        print("\nBook added Successfully..................................!!!!!!\n")
    except:
        print("Error in adding book..................................!!!!!!!!\n")
def displaybooks():
    print("\n--------------------------------------------------------- All Books ----------------------------------------------------------\n")
    try:
        f = open("library.txt", "r")
        lines = f.readlines()
        f.close()
        if len(lines) == 0:
            print("No books found................................!!!!!\n")
            return
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) < 4:
                continue
            bid = parts[0]
            title = parts[1]
            author = parts[2]
            qty = parts[3]
            print("Book Id :", bid)
            print("Title   :", title)
            print("Author  :", author)
            print("Qty     :", qty)
            print("--------------------------------------------------------------------------------------------------------------------")
        print()
    except:
        print("Library file(library.txt) not found................................!!!!\n")
def searchbook():
    name = input("Enter title to search: ").lower()
    found = False
    try:
        f = open("library.txt", "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) < 4:
                continue
            bid = parts[0]
            title = parts[1]
            author = parts[2]
            qty = parts[3]
            if name in title.lower():
                print("\nBook Found Successfully.............................................!!!!!")
                print("Id     :", bid)
                print("Title  :", title)
                print("Author :", author)
                print("Qty    :", qty, "\n")
                found = True
                break
        if not found:
            print("\nBook not found............................................!!!!\n")
    except:
        print("Error in reading library file..................................!!!!\n")
def deletebook():
    did = input("Enter Book ID to delete: ")
    try:
        f = open("library.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("library.txt", "w")
        deleted = False
        for line in lines:
            linestrip = line.strip()
            if linestrip == "":
                continue
            parts = linestrip.split(",")
            if len(parts) < 4:
                f.write(line)
                continue
            bid = parts[0]
            if bid == did:
                deleted = True            
            else:
                f.write(line)
        f.close()
        if deleted:
            print("\nBook deleted Suceesfully...............................!!!!\n")
        else:
            print("\nBook ID not found.........................................!!!!!\n")
    except:
        print("Error in deleting................................!!!!\n")
def updatebook():
    uid = input("Enter Book ID to update: ")
    updated = False
    try:
        f = open("library.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("library.txt", "w")
        for line in lines:
            linestrip = line.strip()
            if (linestrip == ""):
                continue
            parts = linestrip.split(",")
            if (len(parts) < 4):
                f.write(line)
                continue
            bid = parts[0]
            title = parts[1]
            author = parts[2]
            qty = parts[3]
            if (bid == uid):
                print("\n1. Update Title")
                print("2. Update Author")
                print("3. Update Quantity")
                ch = input("Enter choice: ")
                if (ch == "1"):
                    title = input("Enter new title: ")
                elif (ch == "2"):
                    author = input("Enter new author: ")
                elif (ch == "3"):
                    qty = input("Enter new quantity: ")
                print("\nBook updated Successfully......................!!!!!\n")
                updated = True
            f.write(bid + "," + title + "," + author + "," + qty + "\n")
        f.close()
        if not updated:
            print("\nBook ID not found.............................!!!!!\n")
    except:
        print("Error in updating........................................!!!!\n")
def totalbooks():
    try:
        f = open("library.txt", "r")
        lines = f.readlines()
        f.close()
        if len(lines) == 0:
            print("\nNo books available..................................!!!!!!!!!!!!!!\n")
            return
        totaltitles = 0
        totalqty = 0
        for line in lines:
            linestrip = line.strip()
            if linestrip == "":
                continue
            parts = linestrip.split(",")
            if len(parts) < 4:
                continue
            totaltitles = totaltitles + 1
            try:
                q = int(parts[3])
            except:
                q = 0
            totalqty = totalqty + q
        print("\n---------------------------------------- Total Books ---------------------------------------------")
        print("Total Titles :", totaltitles)
        print("Total Quantity:", totalqty)
        print("----------------------------------------------------------------------------------------------------\n")
    except:
        print("Error in counting books...........................................................!!!!!!!!\n")
def issuebook():
    bid=input("Enter Book ID to issue: ")
    sname=input("Enter Student Name: ")
    sid=input("Enter Student ID: ")
    today=datetime.now().date()
    due=today + timedelta(days=7)
    try:
        f=open("library.txt", "r")
        lines=f.readlines()
        f.close()
        f=open("library.txt", "w")
        issued=False
        for line in lines:
            linestrip=line.strip()
            if (linestrip==""):
                continue
            parts=linestrip.split(",")
            if (len(parts)<4):
                f.write(line)
                continue
            bookid=parts[0]
            title=parts[1]
            author=parts[2]
            qty=parts[3]
            if (bookid==bid):
                try:
                    qn=int(qty)
                except:
                    qn=0
                if (qn>0):
                    qn=qn - 1
                    qty=str(qn)
                    issued=True
                    try:
                        f2=open("issued_books.txt", "a")
                        f2.write(bookid + "," + title + "," + sname + "," + sid + "," + str(today) + "," + str(due) + "\n")
                        f2.close()
                    except:
                        print("Error writing issued file......................................!!!!!!!")
                    print("\nBook issued Successfully.............................!!!!!!")
                    print("Student :", sname)
                    print("Issue Date:", today)
                    print("Due Date  :", due, "\n")
                else:
                    print("\nBook out of stock.................................\!!!!!n")
            f.write(bookid + "," + title + "," + author + "," + qty + "\n")
        f.close()
        if not issued:
            print("Book ID not found or not issued..................!!!!!!\n")
    except:
        print("Error in issuing..........................!!!!!!!!!\n")
def returnbook():
    bid=input("Enter Book ID to return: ")
    sname=input("Enter Student Name: ")
    sid=input("Enter Student ID: ")
    today=datetime.now().date()
    try:
        f=open("library.txt", "r")
        lines=f.readlines()
        f.close()
        f=open("library.txt", "w")
        for line in lines:
            linestrip=line.strip()
            if (linestrip==""):
                continue
            parts=linestrip.split(",")
            if (len(parts)<4):
                f.write(line)
                continue
            bookid=parts[0]
            title=parts[1]
            author=parts[2]
            qty=parts[3]
            if (bookid==bid):
                try:
                    qn=int(qty)
                except:
                    qn=0
                qn=qn + 1
                qty=str(qn)
            f.write(bookid + "," + title + "," + author + "," + qty + "\n")
        f.close()
    except:
        print("Error updating quantity...................!!!!!\n")
    try:
        f=open("issued_books.txt", "r")
        lines=f.readlines()
        f.close()
        f=open("issued_books.txt", "w")
        removed=False
        for line in lines:
            linestrip=line.strip()
            if (linestrip==""):
                continue
            parts=linestrip.split(",")
            if (len(parts)!=6):
                f.write(line)
                continue
            ibid=parts[0]
            title=parts[1]
            stname=parts[2]
            stid=parts[3]
            issuedate=parts[4]
            duedate=parts[5]
            if (ibid==bid and stname==sname and stid==sid):
                removed=True
                try:
                    dueobj=datetime.strptime(duedate, "%Y-%m-%d").date()
                except:
                    dueobj=today
                if (today>dueobj):
                    latedays=(today - dueobj).days
                    fine=latedays*5
                    print("\nBook returned late.....................!!!!!!!")
                    print("Late by", latedays, "days")
                    print("Fine to pay: Rs.", fine)
                else:
                    print("\nBook returned on time. No fine.........................!!!!")     
            else:
                f.write(line)
        f.close()
        if removed:
            print("Issued record removed.......................................!!!\n")
        else:
            print("No matching issued record found..............................!!!!\n")
    except:
        print("Error in return process...................!!!!!!!!!!\n")
def viewissued():
    print("\n----------------------------------------- Issued Books --------------------------------------------\n")
    try:
        f = open("issued_books.txt", "r")
        lines = f.readlines()
        f.close()
        if len(lines) == 0:
            print("No books issued..............................!!!!!!!\n")
            return
        for line in lines:
            linestrip = line.strip()
            if linestrip == "":
                continue
            parts = linestrip.split(",")
            if len(parts) != 6:
                continue
            bid = parts[0]
            title = parts[1]
            sname = parts[2]
            sid = parts[3]
            issuedate = parts[4]
            duedate = parts[5]
            print("Book Id   :", bid)
            print("Title     :", title)
            print("Student   :", sname, "(", sid, ")")
            print("Issue Date:", issuedate)
            print("Due Date  :", duedate)
            print("---------------------------------------------------------------------------------------------")
    except:
        print("Error reading issued books...................................!!!!!!!!!\n")
def showduebooks():
    print("\n----------------------------------------------- Due Books -----------------------------------------------------\n")
    today = datetime.now().date()
    try:
        f = open("issued_books.txt", "r")
        lines = f.readlines()
        f.close()
        anydue = False
        for line in lines:
            linestrip = line.strip()
            if linestrip == "":
                continue
            parts = linestrip.split(",")
            if len(parts) != 6:
                continue
            bid = parts[0]
            title = parts[1]
            sname = parts[2]
            sid = parts[3]
            issuedate = parts[4]
            duedate = parts[5]
            try:
                dueobj = datetime.strptime(duedate, "%Y-%m-%d").date()
            except:
                continue
            if dueobj <= today:
                anydue = True
                print("Book Id   :", bid)
                print("Title     :", title)
                print("Student   :", sname, "(", sid, ")")
                print("Issue Date:", issuedate)
                print("Due Date  :", duedate)
                print("-----------------------------------------------------------------------------------------------------")
        if not anydue:
            print("No due books.............................................................................!!!!!!!!!!!!!!!\n")
    except:
        print("Error in showing due books...........................................................!!!!!\n")
def showlatebooks():
    print("\n------------------------------------- Late Books----------------------------------------------------\n")
    today = datetime.now().date()
    try:
        f = open("issued_books.txt", "r")
        lines = f.readlines()
        f.close()
        anylate = False
        for line in lines:
            linestrip = line.strip()
            if linestrip == "":
                continue
            parts = linestrip.split(",")
            if len(parts) != 6:
                continue
            bid = parts[0]
            title = parts[1]
            sname = parts[2]
            sid = parts[3]
            issuedate = parts[4]
            duedate = parts[5]
            try:
                dueobj = datetime.strptime(duedate, "%Y-%m-%d").date()
            except:
                continue
            if today > dueobj:
                anylate = True
                latedays = (today - dueobj).days
                print("Book Id   :", bid)
                print("Title     :", title)
                print("Student   :", sname, "(", sid, ")")
                print("Due Date  :", duedate)
                print("Late by   :", latedays, "days")
                print("--------------------------------------------------------------------------------------------------------")
        if not anylate:
            print("No late books............................................!!!!!!!!!!!!!\n")
    except:
        print("Error in showing late books....................................!!!!!!!!!!\n")
while True:
    print("\n========================== LIBRARY MANAGEMENT SYSTEM ===================")
    print("1. Add Book","                              ","2. Display Books","                              ","3. Search Book")
    print("4. Delete Book","                          ","5. Update Book","                                ","6. Show Total Books")
    print("7. Issue Book","                             ","8. Return Book","                                 ","9. View Issued Books")
    print("10. Show Due Books","                 ","11. Show Late Books","                       ","12. Exit\n")
    choice=input("Enter your choice: ")
    if (choice=="1"):
        addbook()
    elif (choice=="2"):
        displaybooks()
    elif (choice=="3"):
        searchbook()
    elif (choice=="4"):
        deletebook()
    elif (choice=="5"):
        updatebook()
    elif (choice=="6"):
        totalbooks()
    elif (choice=="7"):
        issuebook()
    elif (choice=="8"):
        returnbook()
    elif (choice=="9"):
        viewissued()
    elif (choice=="10"):
        showduebooks()
    elif (choice=="11"):
        showlatebooks()
    elif (choice=="12"):
        print("Program Exited Successfully.............!!!!")
        break
    else:
        print("Invalid choice..............................!!!!!.......Try Again.........!!\n")
