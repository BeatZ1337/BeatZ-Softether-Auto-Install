#BeatZ1337 Softether Auto Install 
#For Ubuntu And Debian
import time, os, colorama

os.system('clear')
print('\033[96m       ___         __           _____       ______       __  __             ')
print('\033[96m      /   | __  __/ /_____     / ___/____  / __/ /____  / /_/ /_  ___  _____')
print('\033[96m     / /| |/ / / / __/ __ \    \__ \/ __ \/ /_/ __/ _ \/ __/ __ \/ _ \/ ___/')
print('\033[96m    / ___ / /_/ / /_/ /_/ /   ___/ / /_/ / __/ /_/  __/ /_/ / / /  __/ /    ')
print('\033[96m   /_/  |_\__,_/\__/\____/   /____/\____/_/  \__/\___/\__/_/ /_/\___/_/')
print('       						 \033[95mBeatZ#1337')
print('  \033[96m1 For Ubuntu/Debian \033[92m2 For Centos')
print('')
print('')
choice = int(input('\033[95mType 1 To Begin:\033[97m'))


if choice == 1:
   print('\033[92mSoftether Auto Install Starting..')
   time.sleep(1)
   os.system('cd /root')
   os.system('apt-get update -y')
   os.system('apt-get install build-essential -y')
   print('\033[92mDownloading Softether Package')
   time.sleep(1)
   os.system('wget https://github.com/SoftEtherVPN/SoftEtherVPN_Stable/releases/download/v4.34-9744-beta/softether-vpnserver-v4.34-9744-beta-2020.03.20-linux-x86-32bit.tar.gz')
   os.system('cd vpnserver')
   os.system('clear')
   print('\033[95mPress \03396m1 \03395m 3 Times To Continue')
   time.sleep(1)
   os.system('make')
   os.system('cd /root')
   os.system('mv vpnserver /usr/local')
   os.system('cd /usr/local/vpnserver')
   os.system('chmod 600 *')
   os.system('chmod 700 vpncmd')
   os.system('chmod 700 vpnserver')
   os.system('wget https://raw.githubusercontent.com/https://github.com/BeatZ1337/BeatZ-Softether-Auto-Install/master/beaters.sh --no-check-certificate mv vpn-server.sh /etc/init.d/vpnserver')
   os.system('cd /etc/init.d/')
   os.system('chmod 755 vpnserver')
   os.system('update-rc.d vpnserver defaults')
   os.system('/etc/init.d/vpnserver start')
   os.system('clear')
   print('\033[95mAuto Install Complete.')
   print('\033[96mMade By BeatZ#1337')
if choice == 2:
   print('\033[92mSoftether Auto Install Starting..')
   time.sleep(1)
   print('\033[95mUpdating Server')
   time.sleep(1)
   os.system('yum update -y')
   os.system('yum groupinstall "development tools" -y')
   os.system('yum install wget -y')
   print('\033[92mDownloading Softether Package')
   time.sleep(1)
   os.system('wget softether-vpnserver-v4.34-9745-rtm-2020.04.05-linux-x86-32bit.tar.gz')
   os.system('cd vpnserver')
   os.system('clear')
   print('\033[95mPress \03396m1 \03395m 3 Times To Continue')
   time.sleep(1)
   os.system('make')
   os.system('cd /root')
   os.system('mv vpnserver /usr/local')
   os.system('cd /usr/local/vpnserver')
   os.system('chmod 600 *')
   os.system('chmod 700 vpncmd')
   os.system('chmod 700 vpnserver')
   os.system('wget https://raw.githubusercontent.com/https://github.com/BeatZ1337/BeatZ-Softether-Auto-Install/master/beaters.sh --no-check-certificate mv beaters.sh')
   os.system('cd /etc/init.d/')
   os.system('chmod 755 vpnserver')
   os.system('chkconfig --add vpnserver')
   os.system('/etc/init.d/vpnserver start')
   os.system('clear')
   print('\033[95mAuto Install Complete.')
   print('\033[96mMade By BeatZ#1337')
else:
	print('\033[95mGoodbye.')


