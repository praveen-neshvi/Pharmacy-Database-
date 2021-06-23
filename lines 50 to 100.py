        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial",13,"bold"),width=14, bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        # ===========Search By========
        lblSearch=Label(ButtonFrame, font=("arial",17,"bold"),text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0,column=5,sticky=w)

        search_combo=ttk.Combobox(ButtonFrame, width=12, font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame, bd=3,relief=RIDGE, width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)


        searchButton=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchButton.grid(row=0,column=3)

        showAll = Button(ButtonFrame, text="SHOW ALL", font=("arial",13,"bold"),width=13, bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        # =====================Label And Entry========================
        lblrefno=Label(DataFrameLeft, font=("arial",12,"bold"),text="Reference no", padx=2)
        lblrefno.grid(row=0,column=5,sticky=w)


        ref_combo=ttk.Combobox(DataFrameLeft, width=27, font=("arial",17,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
