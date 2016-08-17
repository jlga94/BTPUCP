from cassandra.cluster import Cluster

def consult():
	cluster = Cluster()
	session = cluster.connect('btpucp')
	request=session.execute("select * from auxiliar")
	return request
