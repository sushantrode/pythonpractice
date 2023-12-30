from pywebio.input import *

input("This is first Web UI programme try")
x = select("This is a drop down menu", ["Option1", "Option2", "Option 3 ", "Selfie"])
y = checkbox("Multiple Choices!", options=["a", "b", "c", "d"])
z = radio("Select any one", options=["1", "2", "3", "4"])
a = textarea("Text Area", rows=2, placeholder="Write 2 lines about shweta")

print(a)
