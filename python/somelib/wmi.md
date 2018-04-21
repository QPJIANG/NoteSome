# windows cpus	  
	import wmi 
	w=wmi.WMI() 
	cpus=w.Win32_Processor() 
	for u in cpus: 
	  print 'cpu id:',u.ProcessorId
	  print u

# windows net speed	  
	import win32pdh,time
	def netstat() :
			object = "Network Interface"
			items, instances = win32pdh.EnumObjectItems( None, None, object, win32pdh.PERF_DETAIL_WIZARD )
			ifs = {}
			for interface in instances:
					hq = win32pdh.OpenQuery()
					hcs = [ ]
					item = "Bytes Total/sec"
					path = win32pdh.MakeCounterPath( ( None, object, interface, None, 0, item ) )
					hcs.append( win32pdh.AddCounter( hq, path ) )
					win32pdh.CollectQueryData( hq )
					time.sleep( 0.01 )
					win32pdh.CollectQueryData( hq )
					for hc in hcs:
							type, val = win32pdh.GetFormattedCounterValue( hc, win32pdh.PDH_FMT_LONG )
							win32pdh.RemoveCounter( hc )
					win32pdh.CloseQuery( hq )
					ifs[interface] = val
			return ifs
	
	while 1:
			interfaces = netstat()
			for interface in interfaces:
					print interface,' Current netload: ' + str(interfaces[interface]) + 'B/s'
			time.sleep(1)