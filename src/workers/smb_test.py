import smbclient

smbclient.ClientConfig(username=smb_config['smbuser'], password=smb_config['smbpwd'])
smbclient.register_session(smb_config['smbsrv'], username=smb_config['smbuser'], password=smb_config['smbpwd'])
remotepath = r'\\'+smb_config['smbsrv']+'\\' + smb_config['smbshare']+'\\' + smb_config['smbfldr']
smbfiles = smbclient.listdir(remotepath)
smbclient.SambaClient.glob()