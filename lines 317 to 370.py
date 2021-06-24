        
        
        
        self.fetch_dataMed()

        
        # =================Add Medicine Functionality Declaration=====================

        def AddMed(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharma(Ref,Medname) values(%s,%s)",(
                                                                                    self.refMed_var.get(),
                                                                                    self.addmed-var.get(),
            
            
            

                                                                            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Medicine Added")

        def fetch_dataMed(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from pharma")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
                    self.medicine_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        # ==========================MedGetCursor===============================
        def Medget_cursor(self,event=""):
            cursor_row=self.medicine_table.focus()
            content=self.medicine_table.item(cursor_row)
            row=content["values"]
            self.refMed_var.set(row[0])
            self.addMed_var.set(row[1])

        
        def UpdateMed(self):
            if self.refMed_var.get()== or self.addmed_var.get()=="":
                messagebox.showerror("Error","All fields are Required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("Update pharma set MedName=%s where Ref=%s",(
                                                                                self.addmed_var.get(),
                                                                                self.refMed_var.get(),
                                                                            ))
                conn.commit()
                self.fetch_dataMed()
                conn.close()

                messagebox.showinfo("Success","Medicine has been updated")

        def DeleteMed(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
            my_cursor=conn.cursor()  

            sql="delete from pharma where Ref=%s"
            val=(self.refMed_var.get(),)
            my_cursor.execute(sql,val)

            conn.commit()
            self.fetch_dataMed()
            conn.close()

        def ClearMed(self):
            self.refMed_var.set("")
            self.addmed.set("")

