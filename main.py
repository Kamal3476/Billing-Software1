from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk    #pip install pillow
import random
from tkinter import messagebox
import os
import tempfile
from time import strftime

class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        #============Variables=======
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        # Product Categories list
        self.Category=["Select option","Clothing","Life Style","Mobiles"]
        
        # Sub-Categories of Clothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        
        # Brand and Price List
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=800
        self.price_mufti=700
        self.price_spykar=900
        
        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_polo=1300
        self.price_Roadster=1500
        self.price_JackJones=1800
        
        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_Peter=2000
        self.price_Louis=2200
        self.price_Park=1600
        
        
        # Sub-Categoris of LifeStyle
        self.SubCatLifeStyle=['Bath Soap','Face Wash','Face Cream','Hair Oil']
        
        # Bath Soap <----   Brand Name and Price
        self.Bath_soap=['LifeBuy','Lux','Santoor','Pearls']
        self.price_lifeBuy=10
        self.price_lux=20
        self.price_santoor=30
        self.price_pearls=40
        
        # Face Wash <---      Brand name and price
        self.Face_wash=['Himalaya','Cetaphil','Dove','Melia','Gernier']
        self.price_Himalaya=200
        self.price_Cetaphil=800
        self.price_Dove=550
        self.price_Melia=300
        self.price_Gernier=250
        
        # Face creame Brand name and Price
        self.Face_cream=['Fair&Lovely','Ponds','Olay','Gernier']
        self.price_fair=40
        self.price_ponds=30
        self.price_olay=60
        self.price_gernier=20
        
        # Hair Oil <--       Brand name and price
        self.Hair_oil=['Coconut Oil','Jashmin Oil','Bajaj Oil']
        self.price_coco=35
        self.price_jashmin=30
        self.price_bajaj=40
        
        # Sub-Categories of Mobiles
        self.SubCatMobiles=['Iphone','Samsung','Xiaome','Realme','OnePlus']
        
        # Iphone categories and price
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12','Iphone_15','Iphone_16']
        self.price_ix=40000
        self.price_i11=50000
        self.price_i12=60000
        self.price_i15=110000
        self.price_i16=150000
        
        # Samsung categories and price
        self.Samsung=['Samsung M16/F16','Samsung M12/F12','Samsung M21/F21']
        self.price_sM16=16000
        self.price_sM12=10000
        self.price_sM21=21000
        
        # Xiame categories and price
        self.Xiaome=['Redmi 11','Redmi 12','Redmi Pro']
        self.price_r11=9000
        self.price_r12=11000
        self.price_rpro=15000
        
        # RealMe categories and price
        self.Realme=['Realme 12','Realme 13','Realme Pro']
        self.price_rel12=9500
        self.price_rel13=13000
        self.price_relpro=17000
        
        # OnePlus categories and price
        self.OnePlus=['OnePlus 1','OnePlus 2','OnePlus 3']
        self.price_one1=45000
        self.price_one2=50000
        self.price_one3=60000
        
        # Image 1
        img=Image.open("D:\\Billing Software Project\\image\\img1.jpeg")
        img=img.resize((460,130))
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg) 
        lbl_img.place(x=0,y=0,width=460,height=130)
        
        # Image 2
        img_2=Image.open("D:\\Billing Software Project\\image\\img2.jpeg")
        img_2=img_2.resize((500,130))
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=460,y=0,width=500,height=130)
        
        # Image 3
        img_3=Image.open("D:\\Billing Software Project\\image\\img3.jpeg")
        img_3=img_3.resize((450,130))
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=960,y=0,width=450,height=130)
        
        # label for writing BILLING SOFTWARE BY KAMAL at the buttom of the images
        lbl_title=Label(self.root,text="BILLING SOFTWARE BY KAMAL",font=("times new roman",35,"bold"),bg="violet",fg="red")
        lbl_title.place(x=0,y=130,width=1450,height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(lbl_title, font = ('times new roman',16, 'bold'),background= 'pink',foreground="blue")
        lbl.place(x=2,y=0,width=120,height=45)
        time()
        
        # For side border
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1360,height=520)
        
        # Customer Label_Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=9,y=5,width=330,height=140)
        
        # Entry box For customer Mobile number
        self.lbl_mob=Label(Cust_Frame,text="Mobile Number:",font=("times new roman",13,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10, "bold"),width=22)
        self.entry_mob.grid(row=0,column=1)
        
        # Entry box For Customer Name
        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name:",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.textCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=22)
        self.textCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        # Entry box For Customer Email ID
        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email ID:",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.textEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=22)
        self.textEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # Product Label_Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=340,y=5,width=590,height=140)
        
        # Combo Box for Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories:",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=20,state="readonly")
        self.Combo_Category.current(0)    # select categories ko 0 position pe set karne ke liye
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories) # clicked option selected dikhane k liye
        
        # Combo Box for SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory:",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=20)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)  # clicked option selected dikhane k liye 
        
        # Combo Box for Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name:",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=20)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        # Combo Box for Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price:",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=18)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        # Entry Box for Product Quantity
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Quantity:",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=20)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        # Middle Frame 
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=920,height=340)
        
        # Image 1 in Middle Frame 
        img_5=Image.open("D:\\Billing Software Project\\image\\img5.jpeg")
        img_5=img_5.resize((470,230))
        self.photoimg_5=ImageTk.PhotoImage(img_5)
        
        lbl_img_5=Label(MiddleFrame,image=self.photoimg_5)
        lbl_img_5.place(x=0,y=0,width=450,height=230)
        
        # Image 2 in Middle Frame
        img_7=Image.open("D:\\Billing Software Project\\image\\img7.jpeg")
        img_7=img_7.resize((500,230))
        self.photoimg_7=ImageTk.PhotoImage(img_7)
        
        lbl_img_7=Label(MiddleFrame,image=self.photoimg_7)
        lbl_img_7.place(x=450,y=0,width=500,height=230)
        
        # Frame for    --> Search <--            through Bill No.
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=950,y=10,width=500,height=40)
        
        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),fg="white",bg="red",text="Bill Number:")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=2)
        
        # Text -->Entry Box <-- for Bill Search 
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=20)
        self.txt_Entry_Search.grid(row=0,column=2,sticky=W,padx=0)
        
        # Search Button
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=3)
         
        # Label_Frame for Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=940,y=40,width=405,height=350)
         
        # Scroll Bar for Bill Area
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        # Bill counter Label_Frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=390,width=1350,height=120)
        
        # Entry fill label_frame for Sub Total
        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub Total :",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=20)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        # Entry fill label_frame for Gov Tax
        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov. Tax :",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=20)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=6)
        
        # Entry fill label_frame for Total
        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total :",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=20)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        # Button for Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        
        # Button for Generate Bill
        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)
        
        # Button for Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        # Button for Print
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        # Button for Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        
        self.welcome()
        
        self.l=[]
        
    #============================Function Declaration=====================
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome To Ambiance Mini Mall")
        self.textarea.insert(END, f"\n Bill Number:  {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:  {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:  {self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email:  {self.c_email.get()}")
        
        self.textarea.insert(END,"\n======================================================\n")
        self.textarea.insert(END,"\n Products\t\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n======================================================\n")
     
     # Backend work for Add Items   
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Selectthe Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))
            
     # Backend work for Generate Bill       
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text) 
            self.textarea.insert(END,"\n======================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n======================================================")
    
    # Backend work for Save Bill
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully") 
            f1.close()
    
     # Backend work for Print  Button
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    
    # Backend work for SEARCH    
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if  found=='no':
            messagebox.showerror("Error","Invalid Bill No.")
            
    # Backend work on Clear Button
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)

        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
                
                    
        
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Life Style":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)
            
                   
    def Product_add(self,event=""):    
        #for Clothing 
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)    
            
        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
            
        # LifeStyle 
        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Face Wash":
            self.ComboProduct.config(value=self.Face_wash)
            self.ComboProduct.current(0)    
            
        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)   
            
        # Mobiles
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)       
        
        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Xiaome":
            self.ComboProduct.config(value=self.Xiaome)
            self.ComboProduct.current(0)
              
        if self.ComboSubCategory.get()=="Realme":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)
          
        if self.ComboSubCategory.get()=="OnePlus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
            
    # Function for price
    def price(self,event=""):
        
        # Pant                price set
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)  
            
        # T-Shirt                price set
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)          
        
        # Shirt            price set
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)
              
        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)     
          
        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1) 
            
       # Bath Soap              price set
        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.price_lifeBuy)
            self.ComboPrice.current(0)
            self.qty.set(1)     
            
        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)   
            
        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)    
            
        if self.ComboProduct.get()=="Pearls":
            self.ComboPrice.config(value=self.price_pearls)
            self.ComboPrice.current(0)
            self.qty.set(1) 
               
        #  Face Wash              price set 
        if self.ComboProduct.get()=="Himalaya":
            self.ComboPrice.config(value=self.price_Himalaya)
            self.ComboPrice.current(0)
            self.qty.set(1)   
            
        if self.ComboProduct.get()=="Cetaphil":
            self.ComboPrice.config(value=self.price_Cetaphil)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Dove":
            self.ComboPrice.config(value=self.price_Dove)
            self.ComboPrice.current(0)
            self.qty.set(1)   
            
        if self.ComboProduct.get()=="Melia":
            self.ComboPrice.config(value=self.price_Melia)
            self.ComboPrice.current(0)
            self.qty.set(1)   
            
        if self.ComboProduct.get()=="Gernier":
            self.ComboPrice.config(value=self.price_Gernier)
            self.ComboPrice.current(0)
            self.qty.set(1)   
        
        #  Face creame          price set
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1) 
       
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1) 
       
        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1) 
            
        if self.ComboProduct.get()=="Gernier":
            self.ComboPrice.config(value=self.price_gernier)
            self.ComboPrice.current(0)
            self.qty.set(1) 
            
        # Hair Oil             price set    
        if self.ComboProduct.get()=="Coconut Oil":
            self.ComboPrice.config(value=self.price_coco)
            self.ComboPrice.current(0)
            self.qty.set(1)
         
        if self.ComboProduct.get()=="Jashmin Oil":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Bajaj Oil":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)     
            
        # Iphone              price set
        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Iphone_15":
            self.ComboPrice.config(value=self.price_i15)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Iphone_16":
            self.ComboPrice.config(value=self.price_i16)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        # Samsung            price set
        if self.ComboProduct.get()=="Samsung M16/F16":
            self.ComboPrice.config(value=self.price_sM16)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Samsung M12/F12":
            self.ComboPrice.config(value=self.price_sM12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Samsung M21/F21":
            self.ComboPrice.config(value=self.price_sM21)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        
        # Xiaome                 price set
        if self.ComboProduct.get()=="Redmi 11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)    
        
        if self.ComboProduct.get()=="Redmi 12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)    
            
        if self.ComboProduct.get()=="Redmi Pro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # RealMe              price set
        if self.ComboProduct.get()=="Realme 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Realme 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Realme Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)     
         
         # OnePlus                    price set
        if self.ComboProduct.get()=="OnePlus 1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)   
            
        if self.ComboProduct.get()=="OnePlus 2":
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)  
            
        if self.ComboProduct.get()=="OnePlus 3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)  
                 
if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)        
    root.mainloop()