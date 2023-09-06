import streamlit as st
import numpy as np
from generate_sudoku import generate_new_sudoku
from sudoku import is_valid_sudoku

if 'solved_sudoku' not in st.session_state:
    st.session_state.solved_sudoku = None

if 'sudoku_puzzle' not in st.session_state:
    st.session_state.sudoku_puzzle = None

if 'show_sudoku' not in st.session_state:
    st.session_state.show_sudoku = False


def display_sudoku(grid):
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction: row;}</style>', unsafe_allow_html=True)
    for i in range(9):
        if i % 3 == 0 and i > 0:
            st.write('<hr style="background-color: black; height: 2px; margin-top: 5px; margin-bottom: 5px;" />', unsafe_allow_html=True)
        else:
            st.write('<hr style="background-color: grey; height: 1px; margin-top: 5px; margin-bottom: 5px;" />', unsafe_allow_html=True)
        cols = st.columns(9)
        for j in range(9):
            with cols[j].container():
                if grid[i][j] != 0:
                    st.write(
                        f'<div style="border: 1px solid black; width: 40px; height: 40px; display: flex;'
                        f'align-items: center; justify-content: center;">{grid[i][j]}</div>',
                        unsafe_allow_html=True
                    )
                else:
                    cell_key = f"{i}-{j}"
                    cell_value = cols[j].text_input("", key=cell_key)
                    if cell_value != '':
                        cell_value = int(cell_value)
                        if 1 <= cell_value <= 9:
                            grid[i][j] = cell_value
                        else:
                            st.error("Please enter a number between 1 and 9 in each cell.")
                            

st.title("Sudoku")
cols_=st.columns(3)

if cols_[0].button("Check solution"):
    if st.session_state.solved_sudoku :
        if np.array_equal(st.session_state.solved_sudoku, st.session_state.sudoku_puzzle) or is_valid_sudoku(st.session_state.sudoku_puzzle):
            st.success("You solved it!")
        else:
            st.error("Sorry, try again! Here is the solution : ")
            display_sudoku(st.session_state.solved_sudoku)
            st.session_state.show_sudoku= False
    else:
        st.error("Please generate a new game first!")
else:
    pass

if cols_[1].button("Get solution"):
    if st.session_state.solved_sudoku :
        display_sudoku(st.session_state.solved_sudoku)
        st.session_state.show_sudoku = False
    else:
        st.error("Please generate a new game first!")
else:
    pass

if cols_[2].button("New game"):
    solved_sudoku, sudoku_puzzle = generate_new_sudoku()
    st.session_state.solved_sudoku = solved_sudoku
    st.session_state.sudoku_puzzle = sudoku_puzzle
    st.session_state.show_sudoku = True
    #display_sudoku(st.session_state.sudoku_puzzle)
    #print(st.session_state.solved_sudoku)
else:
    pass


    
if st.session_state.show_sudoku:
    display_sudoku(st.session_state.sudoku_puzzle)
        

    
