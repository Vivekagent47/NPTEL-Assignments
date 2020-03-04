# The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.

# Information about books
# Line format: Accession Number~Title

# Information about borrowers
# Line format: Username~Full Name

# Information about checkouts
# Line format: Username~Accession Number~Due Date

# Note: Due Date is in YYYY-MM-DD format.

# You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.
# Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.
# Write a Python program to read the data as described above and print out details about books that have been checked out. Each line should describe to one currently issued book in the following format:

# Due Date~Full Name~Accession Number~Title

# Your output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name. If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.



# Here is a sample input and its corresponding output.

# Sample Input
# Books
# APM-001~Advanced Potion-Making
# GWG-001~Gadding With Ghouls
# APM-002~Advanced Potion-Making
# DMT-001~Defensive Magical Theory
# DMT-003~Defensive Magical Theory
# GWG-002~Gadding With Ghouls
# DMT-002~Defensive Magical Theory
# Borrowers
# SLY2301~Hannah Abbott
# SLY2302~Euan Abercrombie
# SLY2303~Stewart Ackerley
# SLY2304~Bertram Aubrey
# SLY2305~Avery
# SLY2306~Malcolm Baddock
# SLY2307~Marcus Belby
# SLY2308~Katie Bell
# SLY2309~Sirius Orion Black
# Checkouts
# SLY2304~DMT-002~2019-03-27
# SLY2301~GWG-001~2019-03-27
# SLY2308~APM-002~2019-03-14
# SLY2303~DMT-001~2019-04-03
# SLY2301~GWG-002~2019-04-03
# EndOfInput

# Sample Output
# 2019-03-14~Katie Bell~APM-002~Advanced Potion-Making
# 2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory
# 2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls
# 2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls
# 2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory


def sortdates(checkout):
    key = list(map(int,checkout[1].split('-')))
    #print(key)
    key.append(borrow[checkout[0][0]])
    key.append(checkout[0][1])
    # print (tuple(key))
    return tuple(key)

books = dict()
borrow = dict()
checkout = dict()
curr= None
while True:
    line = input()
    if line == 'Books':
        curr= 'Books'
        continue
    elif line == 'Borrowers':
        curr= 'Borrowers'
        continue
    elif line == 'Checkouts':
        curr= 'Checkouts'
        continue
    elif line == 'EndOfInput':
        break
    elif curr== 'Books':
        acc_no,title = line.split('~')
        books[acc_no] = title
    elif curr== 'Borrowers':
        user_name,name = line.split('~')
        borrow[user_name] = name
    elif curr== 'Checkouts':
        user_name,acc_no,due_date = line.split('~')
        checkout[(user_name,acc_no)] = due_date

checkouts = sorted(checkout.items(), key=sortdates)

for checkout in checkouts:
    print(checkout[1] + '~' + borrow[checkout[0][0]] + '~' + checkout[0][1] + '~' + books[checkout[0][1]])