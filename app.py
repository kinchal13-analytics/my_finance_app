import streamlit as st
import matplotlib.pyplot as plot
from db_helper import hello_db,insert_expence,view_all_expences
#start app to ready database and tables
hello_db()
#app title from web
st.title("personal finance tracker")
st.markdown("etxpense manager")
#dataentry form
st.header("data entry")
with st.form('entry form', clear_on_submit=True):
  date=st.date_input("date")
  category=st.selectbox(("category")["food","rent","bills","travel","shopping","entertainment","others"])
  amount=st.number_input(("expense amount"),min_amount=0.0,step=10.0)
  notes=st.text_input("optional")
  submit=st.form_submit_button("save")
  if submit:
    if amount>0:
        insert_expense(str(date),category,amount,notes)
        st.success(f'congratulations {amount} expense is saved to {category}')
    else:
        st.error("please enter a number grater then zero")
  #data visulaisation
  st.header(" your expenses")
  df=view_all_expences()
  if not df.empty:
    total_spend=df["amount"].sum()
    st.markdown(f"total spend is {total_spend}")
    #datatable
    st.subheader("list your expenses")
    st.dataframe(df[["date","category","amount","notes"]])
    #chartwise data
    st.subheader("chartwise data(pie chart)")
    cat_df=df.groupby(category)['amount'].sum().reset_index()
    fig.ax= plot.subplots()
    ax.pie(cat_df["amount"],lables=cat_df["category"],autopct="%1.2f%%")
    ax.axis=("equal")
    st.pyplot(fig)
  else:
    st.into("no expense has been added yet.add your first expense using the form above")
