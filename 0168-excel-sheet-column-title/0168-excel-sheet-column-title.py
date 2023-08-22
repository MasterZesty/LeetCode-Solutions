class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # as we have 10 based system in general way here
        # we are having 26 based system
        
        if columnNumber <= 26:
            return chr(columnNumber + 64)
        else:
            column_title = ""
            while columnNumber > 0:
                print(f"number is : {columnNumber} ")
                columnNumber, remainder = divmod(columnNumber-1, 26)
                print(f"number is : {columnNumber} and remainder: {remainder}")
                column_title = chr(remainder + 65) + column_title
                print(f"column_title : {column_title}")
                
            print(f"final column_title {column_title}")
            return column_title