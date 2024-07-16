# try:
#     raise MemoryError('Memory Error')
# except MemoryError as e:
#     print(e)

# # exception using class

# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def print_exception(self):
#         print("User defined exception: ",self.msg)

# try:
#     raise Accident('crash between two caes')
# except Accident as e:
#     e.print_exception()

# # raise exception and finally
# def process_file():
#     try:
#         f=open('youtube.txt')
#         x=1/0
#     except FileNotFoundError as e:
#         print('inside except')
#     finally:
#         print('cleaning up file')
#         f.close()