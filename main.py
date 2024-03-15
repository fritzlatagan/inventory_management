from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
import pymysql
import csv
from datetime import datetime
import re

#Initializes main window
main_window=tkinter.Tk()
main_window.title("MES Inventory Management")
main_window.geometry("1165x840")
main_window.configure(background="#46A0F9")
data_table=ttk.Treeview(main_window, show='headings', height=20)
style=ttk.Style()

#Some used variables
# Initialize placeholderArray with enough elements
placeholderArray = ['', '', '', '', '', '', '']
numeric='1234567890'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Mainly Responsible For Connecting to Localhost SQL Database
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='inventory_management'
    )
    print(f"Connected to MySQL server: {conn}")
    return conn

conn = connection()
cursor = conn.cursor()

for i in range(0, 5):
    placeholderArray[i] = tkinter.StringVar()

# Reads the database items
def read():
    try:
        cursor.connection.ping()
        sql = """
SELECT
    si.serial_number,
    si.property_id,
    si.room_id,
    si.item_specification,
    a.acquisition_date, 
    pc.custodian_id,
    des.description_id
FROM
    Serialized_Items AS si
LEFT JOIN Acquisition_Details AS ad ON ad.property_id = si.property_id
LEFT JOIN Acquisition AS a ON a.acquisition_id = ad.acquisition_id
LEFT JOIN Property_Custodian AS pc ON a.custodian_id = pc.custodian_id  
LEFT JOIN Description AS des ON si.description_id = des.description_id
ORDER BY
    si.serial_number DESC
  """

        cursor.execute(sql)
        results = cursor.fetchall()
        return results  # Return the fetched results
    except (pymysql.err.OperationalError, ConnectionError) as err:
        print("Error connecting to database:", err)
        messagebox.showerror("Error", "Failed to connect to database. Please check your connection details.")
        return []  # Return an empty list if an error occurs
    finally:
        conn.close()


# Refreshes the table everytime an action is performed
def refreshTable():
    for data in data_table.get_children():
        data_table.delete(data)
    for array in read():
        data_table.insert(parent='', index='end', iid=array, text="", values=(array), tag="bg_color")
    data_table.tag_configure('bg_color', background="#7CB1E5")
    data_table.pack()

# Gives values to placeholderarray
def setph(word, num):
    for ph in range(0, 5):
        if ph == num:
            placeholderArray[ph].set(word)

#Adds/Saves items in entry to the database
def save():
    # Get values from user input
    serial_number = serialNumberEntry.get()
    property_id = propertyIdEntry.get()
    room_id = roomIdEntry.get()
    item_specification = itemSpecificationEntry.get()
    acquisition_date = acquisitionDateEntry.get()
    custodian_id = custodianIdEntry.get()
    description_id = descriptionIdEntry.get()
    
    # Regular expressions for validation
    alphanumeric_regex = re.compile(r'^[a-zA-Z0-9]+$')
    numeric_regex = re.compile(r'^[0-9]+$')
    
    # Input validation
    if not (serial_number and serial_number.strip()) or not (property_id and property_id.strip()) or not (room_id and room_id.strip()) or not (item_specification and item_specification.strip()) or not (acquisition_date and acquisition_date.strip()) or not (custodian_id and custodian_id.strip()) or not (description_id and description_id.strip()):
        messagebox.showwarning("", "Please fill up all entries")
        return

    if len(serial_number) != 16 or not alphanumeric_regex.match(serial_number):
        messagebox.showwarning("", "Invalid serial number format")
        return

    if not numeric_regex.match(property_id) or len(property_id) > 3:
        messagebox.showwarning("", "Invalid property ID")
        return

    if not numeric_regex.match(room_id) or len(room_id) > 3:
        messagebox.showwarning("", "Invalid room ID")
        return

    if len(item_specification) > 50:
        messagebox.showwarning("", "Item specification exceeds maximum length")
        return

    try:
        cursor.connection.ping()
        sql = f"INSERT INTO Serialized_Items (serial_number, property_id, room_id, item_specification, acquisition_date, custodian_id, description_id) VALUES ('{serial_number}', '{property_id}', '{room_id}', '{item_specification}', '{acquisition_date}', '{custodian_id}', '{description_id}')"
        cursor.execute(sql)
        conn.commit()
        refreshTable()
        messagebox.showinfo("", "Data saved successfully")
    except Exception as e:
        print(e)
        messagebox.showwarning("", f"Error while saving: {str(e)}")

    


# Updates the selected item with input validation
def update():
    selectedItemId = ''
    try:
        selectedItem = data_table.selection()[0]
        selectedItemId = str(data_table.item(selectedItem)['values'][0])
    except IndexError:
        messagebox.showwarning("", "Please select a data row")
        return

    # Get updated values from entry fields
    serial_number = str(serialNumberEntry.get())
    property_id = str(propertyIdEntry.get())
    room_id = str(roomIdEntry.get())
    item_specification = str(itemSpecificationEntry.get())
    acquisition_date = str(acquisitionDateEntry.get())
    custodian_id = str(custodianIdEntry.get())
    description_id = str(descriptionIdEntry.get())

    # Regular expressions for validation
    alphanumeric_regex = re.compile(r'^[a-zA-Z0-9]+$')
    numeric_regex = re.compile(r'^[0-9]+$')

    # Input validation
    if not (serial_number and serial_number.strip()) or not (property_id and property_id.strip()) or not (room_id and room_id.strip()) or not (item_specification and item_specification.strip()) or not (acquisition_date and acquisition_date.strip()) or not (custodian_id and custodian_id.strip()) or not (description_id and description_id.strip()):
        messagebox.showwarning("", "Please fill up all entries")
        return

    if len(serial_number) != 16 or not alphanumeric_regex.match(serial_number):
        messagebox.showwarning("", "Invalid serial number format")
        return

    if not numeric_regex.match(property_id) or len(property_id) > 3:
        messagebox.showwarning("", "Invalid property ID")
        return

    if not numeric_regex.match(room_id) or len(room_id) > 3:
        messagebox.showwarning("", "Invalid room ID")
        return

    if len(item_specification) > 50:
        messagebox.showwarning("", "Item specification exceeds maximum length")
        return

    try:
        cursor.connection.ping()
        sql = f"UPDATE Serialized_Items SET property_id = '{property_id}', room_id = '{room_id}', item_specification = '{item_specification}', acquisition_date = '{acquisition_date}', custodian_id = '{custodian_id}', description_id = '{description_id}' WHERE serial_number = '{selectedItemId}'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        messagebox.showinfo("", "Data updated successfully")
        refreshTable()
    except Exception as err:
        messagebox.showwarning("", f"Error occurred while updating data: {str(err)}")


# Deletes the selected item
def delete():
    try:
        selectedItem = data_table.selection()[0]
        decision = messagebox.askquestion("", "Delete the selected data?")
        if decision == 'yes':
            itemId = str(data_table.item(selectedItem)['values'][0])
            cursor.connection.ping()
            sql = f"DELETE FROM Serialized_Items WHERE serial_number = '{itemId}'"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            messagebox.showinfo("", "Data has been successfully deleted")
            refreshTable()
    except IndexError:
        messagebox.showwarning("", "Please select a data row")

# Used to select an item
def select():
    try:
        selectedItem = data_table.selection()[0]
        itemId = str(data_table.item(selectedItem)['values'][0])
        property_id = str(data_table.item(selectedItem)['values'][1])
        room_id = str(data_table.item(selectedItem)['values'][2])
        item_specification = str(data_table.item(selectedItem)['values'][3])
        acquisition_date = str(data_table.item(selectedItem)['values'][4])
        custodian_id = str(data_table.item(selectedItem)['values'][5])
        description_id = str(data_table.item(selectedItem)['values'][6])
        setph(itemId, 0)
        setph(property_id, 1)
        setph(room_id, 2)
        setph(item_specification, 3)
        setph(acquisition_date, 4)
        setph(custodian_id, 5)
        setph(description_id, 6)
    except IndexError:
        messagebox.showwarning("", "Please select a data row")

# Finds an item based on one of the user's entry
def find():
    # Get search criteria from entry fields
    serial_number = str(serialNumberEntry.get())
    property_id = str(propertyIdEntry.get())
    room_id = str(roomIdEntry.get())
    item_specification = str(itemSpecificationEntry.get())
    acquisition_date = str(acquisitionDateEntry.get())
    custodian_id = str(custodianIdEntry.get())
    description_id = str(descriptionIdEntry.get())

    cursor.connection.ping()
    sql = f"SELECT serial_number, property_id, room_id, item_specification, acquisition_date, custodian_id, description_id FROM Serialized_Items WHERE serial_number LIKE '%{serial_number}%' AND property_id LIKE '%{property_id}%' AND room_id LIKE '%{room_id}%' AND item_specification LIKE '%{item_specification}%' AND acquisition_date LIKE '%{acquisition_date}%' AND custodian_id LIKE '%{custodian_id}%' AND description_id LIKE '%{description_id}%'"
    
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        setph(result[0][0], 0)
        setph(result[0][1], 1)
        setph(result[0][2], 2)
        setph(result[0][3], 3)
        setph(result[0][4], 4)
        setph(result[0][5], 5)
        setph(result[0][6], 6)
    else:
        messagebox.showwarning("", "No data found")

# Clears the entry form
def clear():
    for num in range(0, 5):
        setph('', num)

# Exports the database to an excel file
def exportExcel():
    cursor.connection.ping()
    sql = "SELECT serial_number, property_id, room_id, item_specification, acquisition_date, custodian_id, description_id FROM Serialized_Items ORDER BY serial_number DESC"
    cursor.execute(sql)
    dataraw = cursor.fetchall()
    date = str(datetime.now())
    date = date.replace(' ', '_')
    date = date.replace(':', '-')
    dateFinal = date[0:16]
    with open("Serialized_Items_"+dateFinal+".csv", 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in dataraw:
            w.writerow(record)
    print("saved: Serialized_Items_"+dateFinal+".csv")
    conn.commit()
    conn.close()
    messagebox.showinfo("", "Excel file downloaded")

#Frame formating for succeding objects
frame=tkinter.Frame(main_window,bg="#7CB1E5")
frame.pack()

#button color
btnColor="#1355B5"

#Actions Frame
actions_frame=tkinter.LabelFrame(frame, text="Actions", borderwidth=5)
actions_frame.grid(row=1, column=0, sticky="w", padx=[20, 1500], pady=[10, 10], ipadx=[6])

saveBtn=Button(actions_frame, text="SAVE", width=10, borderwidth=3, bg=btnColor, fg='white', command=save)
updateBtn=Button(actions_frame, text="UPDATE", width=10, borderwidth=3, bg=btnColor, fg='white', command=update)
deleteBtn=Button(actions_frame, text="DELETE", width=10, borderwidth=3, bg=btnColor, fg='white', command=delete)
selectBtn=Button(actions_frame, text="SELECT", width=10, borderwidth=3, bg=btnColor, fg='white', command=select)
findBtn=Button(actions_frame, text="FIND", width=10, borderwidth=3, bg=btnColor, fg='white', command=find)
clearBtn=Button(actions_frame, text="CLEAR", width=10, borderwidth=3, bg=btnColor, fg='white', command=clear)
exportBtn=Button(actions_frame, text="EXPORT EXCEL", width=15, borderwidth=3, bg=btnColor, fg='white', command=exportExcel)

saveBtn.grid(row=0,column=1,padx=5,pady=5)
updateBtn.grid(row=0,column=2,padx=5,pady=5)
deleteBtn.grid(row=0,column=3,padx=5,pady=5)
selectBtn.grid(row=0,column=5,padx=[430,5],pady=5)
findBtn.grid(row=0,column=4,padx=5,pady=5)
clearBtn.grid(row=0,column=0,padx=5,pady=5)
exportBtn.grid(row=0,column=6,padx=5,pady=5)

#Entries Frame
entriesFrame=tkinter.LabelFrame(frame,text="Entry",borderwidth=5)
entriesFrame.grid(row=0,column=0,sticky="w",padx=[20,1500],pady=[10,0],ipadx=[6])

serialNumberLabel=Label(entriesFrame,text="Serial Number",anchor="e",width=15)
propertyIdLabel=Label(entriesFrame,text="Property ID",anchor="e",width=15)
roomIdLabel=Label(entriesFrame,text="Room ID",anchor="e",width=15)
itemSpecificationLabel=Label(entriesFrame,text="Item Specification",anchor="e",width=15)
acquisitionDateLabel=Label(entriesFrame,text="Acquisition Date",anchor="e",width=15)
custodianIdLabel=Label(entriesFrame,text="Custodian ID",anchor="e",width=15)
descriptionIdLabel=Label(entriesFrame,text="Description ID",anchor="e",width=15)

serialNumberLabel.grid(row=0,column=0,padx=15)
propertyIdLabel.grid(row=1,column=0,padx=15)
roomIdLabel.grid(row=2,column=0,padx=15)
itemSpecificationLabel.grid(row=3,column=0,padx=15)
acquisitionDateLabel.grid(row=4,column=0,padx=15)

serialNumberEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[0])
propertyIdEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[1])
roomIdEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[2])
itemSpecificationEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[3])
acquisitionDateEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[4])
custodianIdEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[5])
descriptionIdEntry=Entry(entriesFrame,width=50,textvariable=placeholderArray[6])

serialNumberEntry.grid(row=0,column=2,padx=5,pady=5)
propertyIdEntry.grid(row=1,column=2,padx=5,pady=5)
roomIdEntry.grid(row=2,column=2,padx=5,pady=5)
itemSpecificationEntry.grid(row=3,column=2,padx=5,pady=5)
acquisitionDateEntry.grid(row=4,column=2,padx=5,pady=5)

custodianIdLabel.grid(row=5,column=0,padx=15)
descriptionIdLabel.grid(row=6,column=0,padx=15)

custodianIdEntry.grid(row=5,column=2,padx=5,pady=5)
descriptionIdEntry.grid(row=6,column=2,padx=5,pady=5)


#LOGO / IMAGE
logo = Image.open("me_logo.png")
test = ImageTk.PhotoImage(logo)
logo_hold = tkinter.Label(image=test)
logo_hold.image = test
logo_hold.place(x=625, y=10)

#Calls refreshTable()
refreshTable()

#Closing of mainoop
main_window.resizable(False,False)
main_window.mainloop()