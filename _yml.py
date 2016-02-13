import sublime, sublime_plugin
import os

here = os.path.abspath(os.path.dirname(__file__))

if os.path.join("Packages", "User") in here:
	pop up and ask user if this file shud be loaded as yml if yes
	open file as .yml
	on_save revert back to json
else:
	ignore



def xxx(filePath):
	# lazy read for big (os.stat) file?
	with open(filePath, mode="rt", encoding="UTF-8") as fh:
		o = json.load(fh.read)
	with open(tempFile, mode="wt", encoding"UTF-8") as fh:
		fh.write(json2yaml(o))
	return








TAB = "    "
LIST= "  - "
def yaml2json(text):
	def analyse(start):
		tabs = start.count(TAB, start.index(":"))
		if start[tabs:tabs+3] is LIST:
			return tabs, True
		else:
			return tabs, False
	lines = text.split(NEW_LINE)	# const but platform dependent
	_.rstrip(" ") for _ in lines
	dataStructTracker = ["obj"]
	jsonStr = "{"	# no syntactic beautification, thank you
	
	for i in range(len(lines)):
		pre, sep, post = line[i].partition(":")
		currDepth = pre.count(TAB)	# compare old n curr
		if currDepth < old_Depth:	# 10;13;17;21;27
			actions = [dataStructTracker.pop() for _ in range(old_Depth-currDepth)]
			jsonStr+= "".join(["]" for _ in actions if _ is "list" else "}"])
		if post not None:	#2-6;11;12;14;15;16;20;23;24;26;28
			# its a simple key value pair
			jsonStr+= '"' + pre + '":' + (lambda: post if type(post) is int or type(post) is float or post is "true" else '"'+post+'"')
		else:	# 7;8;9
			# implies this key (i.e. pre's present value) represents a list or
			# a sub-object NOT a comon key value pair, : won't be found anymore
			i+= 1
			nextDepth = lines[i].count(TAB)
			if nextDepth < currDepth:
				# ERROR or NULL value to key depending on strictness criterion,, gotta dataStruct.pop next-currTIMEs
			elif nextDepth is curr:
				if lines[i+1][nextDepth:nextDepth+3] is LIST:
					dataStructTracker.append("list")
					jsonStr+= "["
					if lines[i+2].count(TAB) - lines[i+1].count(TAB) is 1:
						dataStructTracker.append("obj")
						jsonStr+= "{"
				else:
					# ??? error or same as simple key value pair
			elif nextDepth - currDepth is 1 and ":" in lines[i+1]:
				dataStructTracker.append("obj")
				jsonStr+= "{"
			else:
				# ??? error
		old_Depth = currDepth
	
	# add commas at end of all-but-last-of-its-kind-section-closers
	
	return jsonStr








