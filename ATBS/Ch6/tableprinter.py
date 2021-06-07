###############################################################################
########### TablePrinter.py - Prints right justified tables ###################
####### Practice Project Chapter 6 - Automate the Boring Stuff ################
###############################################################################
# Input is a list of lists of strings.
# all inner lists always contain the same number of strings
# Print a table where each inner list is a column. All strings in the table
# must be right justified. The columnwidth must equal the length of the
# longest string



def printTable(table):
    colWidths = [0] * len(table) # creates a list with a number of 0s equal to
    # the number of inner lists in input.


    # loop over outer list and for each element of the outer list loop over
    # the elements of that inner list. find longest element of inner list and
    # save it in list colWidths
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])



    #find largest value in colWidths as input for rjust()
    maxColWidth = max(colWidths)


    # Take all first/second/third... elements of the inner lists and concatenate
    # them to a string. (One string per column of formatted table)
    # Rjustify that string with the already calculated maximum
    # length of strings in the input.

    # length of inner list = number of rows of the formatted table (outer loop)
    for i in range(len(table[1])): # all inner lists have the same length.
        column = ''
        for j in range(len(table)): # loop over all inner lists

            # take the entry of the inner list and add it to the column
            innerList_entry = table[j][i].rjust(maxColWidth)

            column += innerList_entry
        # print the result with a linebreak after each column
        print(column + "\n")


################################################################################


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
