@ns db

@method listall
#@parser accumulateList(directory,file)
@parser nestedList
@reducer dbList

@method listallinfo
@parser accumulateList(directory,file)

@method list
@arguments dbList
@parser nestedList

@method count
@parser list

@method find
@parser songs

@method findadd

@method search
@parser songs

@method searchadd

@method searchaddpl

@method lsinfo
@parser dbListInfo
@reducer dbListInfo

@method listfiles
@parser dbListInfo

@method readcomments
@parser object

@method rescan
@parser object

@method update
@parser object

@method getfingerprint
@parser object

@method albumart
@use albumart

@method albumartWhole
@use albumartWhole