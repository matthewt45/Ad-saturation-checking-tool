Ad saturation checking tool

WIP

to use write desired keywords into keywords.txt file and run the tool.
The tool will first compare the list of keywords to previously searched keywords in usedKeywords.txt this allows for persitance.
The resulting set will then be iterated through and seached with selenium whereby google-shopping links will be collected.
After collecting the links selenium will then iterate through each website and take a screenshot after the page has loaded.
After all the shopping links have been iterated through or the specified amount of sites per keyword is reached the next keyword will be loaded in at this stage the previous keyword is marked as used and stored in usedKeywords.txt.
