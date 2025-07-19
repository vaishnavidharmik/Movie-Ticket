import streamlit as st
import os

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 class='main-title'>🍿 Welcome to <span>CineStream Booking</span></h1><hr>", unsafe_allow_html=True)

# Movies data
movies = [
    {
        "title": "Pathaan",
        "poster": "posters/Pathaan.jpg",
        "trailer": "https://www.youtube.com/watch?v=vqu4z34wENw",
        "price": 280
    },
    {
        "title": "Pushpa",
        "poster": "posters/Pushpa.jpg",
        "trailer": "https://www.youtube.com/watch?v=Q1NKMPhP8PY",
        "price": 260
    },
    {
        "title": "Jailer",
        "poster": "posters/Jailer.jpg",
        "trailer": "https://www.youtube.com/watch?v=K2QkT9oP7LQ",
        "price": 270
    },
    {
        "title": "Animal",
        "poster": "posters/Animal.jpg",
        "trailer": "https://www.youtube.com/watch?v=2ZlUnLbP4xY",
        "price": 300
    }
]

# Initialize session state to track bookings
if 'book_clicked' not in st.session_state:
    st.session_state.book_clicked = None

# 2 movies per row
for i in range(0, len(movies), 2):
    cols = st.columns(2)
    for col, movie in zip(cols, movies[i:i+2]):
        with col:
            poster_path = movie["poster"]
            if os.path.exists(poster_path):
                st.image(poster_path, use_container_width=True)
            else:
                st.error("Poster not found!")

            st.markdown(f"<div class='movie-title'>{movie['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='movie-price'>🎟 ₹{movie['price']}</div>", unsafe_allow_html=True)

            if st.button(f"🎥 Trailer - {movie['title']}", key=f"trailer_{movie['title']}"):
                st.video(movie["trailer"])

            if st.button("🎟️ Book", key=f"book_btn_{movie['title']}"):
                st.session_state.book_clicked = movie['title']

            if st.session_state.book_clicked == movie['title']:
                st.markdown("### 📝 Fill Your Booking Details")
                name = st.text_input("👤 Your Name", key=f"name_{movie['title']}")
                tickets = st.number_input("🎫 Number of Tickets", min_value=1, step=1, key=f"tickets_{movie['title']}")
                food = st.selectbox("🍔 Add Food Combo", ["None", "Popcorn", "Cold Drink", "Burger Combo"], key=f"food_{movie['title']}")
                if st.button("✅ Confirm Booking", key=f"confirm_{movie['title']}"):
                    total = movie['price'] * tickets
                    st.success(f"Thanks {name}! You booked {tickets} tickets for {movie['title']} 🍿\nTotal: ₹{total}")
