import random
dates={"Contrabands of War":"1860s","Emancipation Proclamtion":"1863","Cotton Gin":"1793","Positive Good":"1840s","Republican Motherhood":"1800s","Haitian Revolution":"1791-1804","Gradual Emancipation":"1777","John Brown":"1856-1859","Popular Sovereignty":"1854","Dredd Scott":"1856","William Walker":"1840s","Free Labor Ideology":"1800s","Uncle Tom's Cabin":"1852","Filibuster":"1850s","Election of ___":"1860","Special Field Order 15":"1865","Compromise of ___":"1850","The Missouri Compromise":"1820","Democratic-Republican Societes":"1800s","Wilmot Proviso":"1846","Interstate Slave Trade":"1790s-1800s","Yeoman Farmers":"1800s","Wage Labor":"1800s","The Whiskey Rebellion":"1794","Tarrif of Abominations":"1828","The Bank War":"1833","Peggy O'Neal":"1820s","Universal White Male Suffrage":"1820","Julia Chinn(Eaton Affair)-Birth to Death":"1790-1836","Civilization Program":"1795","James L. McDonald":"1800s","Transportation Revolution":"1810s-1820s","Stephen Austin":"1820s","Sam Patch":"1810s-1828","Lowell Girls":"1800s","Madeira":"Late 1700s","Treating":"1800s","The Temperance Movement":"1800s","The Northwest Ordinance":"1785 and 1787","The Battle of New Orleans":"1815","War of a Thousand Deserts":"1840s","Louisiana Purchase":"1803"}
mode=input("Flash Card Mode[press f] or List Mode[press l]: ")


if mode=="f":
  dontstop="y"
  
  while dontstop=="y" and len(dates)>0:
    print()
    curr_date=list(dates)[random.randint(0,len(dates)-1)]
    print(".: "+curr_date+" :.")
    check_date=input("Enter a date,era,era range,or date range: ")
    if check_date==dates[curr_date]:
      del dates[curr_date]
      print("CORRECT!")
      print()
    else:
      print()
      print("WRONG! :(")
      print("The correct answer was: "+dates[curr_date])
      dontstop=input("Keep going?(y for yes|n for no):")
      print()
else:
  for i in dates:
    curr_date=i
    print(".: "+curr_date+" :.")
    check_date=input("Enter a date,era,era range,or date range: ")
    if check_date==dates[curr_date]:
      print("CORRECT!")
      print()
    else:
      print()
      print("WRONG! :(")
      print("The correct answer was: "+dates[curr_date])
      print()
