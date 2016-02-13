class FileHandler():
	""" lazy read 'num_lines' lines from filePath
	to avoid overwhelming the RAM, most importantly
	it runs only when asked for """
	
	filePath, num_lines = str(), int()
	
	def setVarValues(self):
		filePath = input()
		num_lines= input()
		moreLines = nLineReader()
		return
	
	def nLineReader():
		with open(filePath, mode"rt", encoding="UTF-8") as fh:
			yield fh.readlines(num_lines)
	
	def giveMeMore(self):
		try:
			x = next(moreLines)
		except StopIteration:
			return None
		return x

class YAML_to_JSON():
	jsonStr = "{"
	ds = ['o']	# data structure tracker list, either oBJECT or lIST
	TAB = "    "
	LIST= "  - "
	onStrictMode = False
	
	def run(self):
		FileHandler.setVarValues()
		while True:
			x = FileHandler.giveMeMore()
			if x is None:
				break
			else:
				processThese(x)
		return
	
	def dsu(*addWhat):
		if len(addWhat) is 0:	# or addWhat is None
			temp = ds.pop()
			jsonStr+= '}' if temp is 'o' else ']'
		elif len(addWhat) is 1:
			ds.append(addWhat[0])
			jsonStr+= '{' if addWhat[0] is 'o' else '['
		else:
			pass
		return
	
	def processThese(lines):
		_.rstrip(" ") for _ in lines	# needed?
		for i, thisLine in enumerate(lines):	# is not len(lines) bound to be 100 by default
			if i <= len(lines)-3:	# 2-3 being the seekAhead offset
				# wooow, what to do??? FileHandler.giveMeMore()? but where to store it?
			
			isList = True if thisLine.lstrip(TAB).startswith(LIST) else False
			realDepth = thisLine.count(TAB) + int(isList)
			if realDepth < len(ds):	# if depth decreases ELSE depth is same or increases
				while realDepth-len(ds) not 0:
					dsu()
			elif realDepth is len(ds):
				if ds[-1] not '[' and  ':' in thisLine:
					pre, sep, post = thisLine.partition(":")
					if post is None:
						promise_broken = True
					else:
						# simple key value pair
						jsonStr+= '"' + pre + '":' + (lambda: post if type(post) is int or type(post) is float or post is "true" else '"'+post+'"')
				else:
					ERROR
			else:	# realDepth > len(ds)
				if promise_broken:	# value for last line,,, what if nested object???
					# implies this line must be either a list or a child obj
				else:
					?
			if LIST in thisLine[realDepth:
				type(idealDepth) is int:
				
			











