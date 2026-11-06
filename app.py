import streamlit as st
from db_helper import hello_db,insert_expense,view_all_expenses
#start app to ready database and tables
hello_db()
#app title from web
st.title("personal finance tracker")
st.markdown("etxpense manager")
#dataentry form
st.header("data entry")
with st.form('entry form', clear_on_submit=True):
  date=st.date_input("date")
  category=st.selectbox("category",["food","rent","bills","travel","shopping","entertainment","others"])
  amount=st.number_input(("expense amount"),min_value=0.0,step=10.0)
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
  df=view_all_expenses()
  if not df.empty:
    df["DATE"] = pd.to_datetime(df["DATE"])
    start_date = st.date_input("Kab se dekhna hai?")
    end_date = st.date_input("Kab tak dekhna hai?")

    df = df[(df["DATE"] >= pd.to_datetime(start_date)) & (df["DATE"] <= pd.to_datetime(end_date))]
    total_spend=df["AMOUNT"].sum()
    st.markdown(f"total spend is {total_spend}")
    #datatable
    st.subheader("list your expenses")
    st.dataframe(df[["DATE","CATEGORY","AMOUNT","NOTES"]])
    #chartwise data
    st.subheader("chartwise data(pie chart)")
    cat_df=df.groupby("CATEGORY")['AMOUNT'].sum().reset_index()
    st.bar_chart(cat_df.set_index("CATEGORY")["AMOUNT"])
  else:
    st.info("no expense has been added yet.add your first expense using the form above")
