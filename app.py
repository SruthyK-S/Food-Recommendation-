import streamlit as st

st.set_page_config(
    page_title="Recipe Generator",
    page_icon="🍓",
    layout= "wide",
    initial_sidebar_state= "auto"
)
ingredients = st.text_input(label = "Enter ingredients separated by space")

if st.button('Show Recipe'):
    if ingredients:
        ingredients_list = ingredients.split(" ")
        for i in ingredients_list:
            st.write("* " + i + "\n")
    

# ingredients = st.text_area("Enter ingredients separated by commas", height= 10,value= "* " ,key = "value")

images = ["https://images.pexels.com/photos/1435735/pexels-photo-1435735.jpeg", 
          "https://images.pexels.com/photos/1854652/pexels-photo-1854652.jpeg?auto=compress&cs=tinysrgb&w=600", 
          "https://images.pexels.com/photos/3186654/pexels-photo-3186654.jpeg?auto=compress&cs=tinysrgb&w=600"]

col = st.columns(3)
for i in range(3):
    with col[i]:
        st.image(images[2-i])
        if i == 0:
            st.write("""No more "what's for dinner?" dread. Find hidden gems and forgotten favorites, 
                     rediscover the joy of cooking, or explore new cuisines with confidence.""")