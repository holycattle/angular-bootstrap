import os, argparse, shutil, errno

#get directory of angular-seed
angular_seed_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'angular-seed')

parser = argparse.ArgumentParser(description='Bootstrap your AngularJS apps.')
parser.add_argument('-s', '--start', type=str, help='starts a project; requires the name of the project')

args = parser.parse_args()

if args.start:
	if os.path.isdir(angular_seed_dir): #check if angular-seed exists
		print 'creating project %s...' %(args.start)
		shutil.copytree(angular_seed_dir, os.path.join(os.getcwd(), args.start))
		print 'done!'
	else:
		print 'angular-seed doesn\'t exist yet!'
		try:
			os.system('git clone https://github.com/angular/angular-seed.git') #requires git
		except OSError as err:
			print 'Error cloning angular-seed from Github. Please make sure that Git is installed properly.'