import ipaddress
import re

app_loop = ''
while(app_loop!= 'n'):
    # input_IP = '192.168.0.129'
    # mask1 = '24'
    # mask2 = '255.255.255.0'
    input_IP = input("Enter the IP address \t: ")
    if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",input_IP):
        octet_list = input_IP.split('.')
        if (
            len(octet_list) == 4 
            and 1 <= int(octet_list[0]) <= 223 
            and int(octet_list[0]) != 127 
            and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254)
            and 0 <= int(octet_list[1]) <= 255 
            and 0 <= int(octet_list[2]) <= 255 
            and 0 <= int(octet_list[3]) <= 255
            ):
            mask_input = input("Enter subnet mask \t: ")
            if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",mask_input):   
                # following code will strip the subnet mask 
                # and calculate the number of subnets and number of hosts
                str_masksplit = mask_input.split('.')
                int_Masksplit = [int(mask) for mask in str_masksplit]
                bin_masksplit = [(bin(m).lstrip('0b')).zfill(8) for m in int_Masksplit]
                bin_mask = ''.join(bin_masksplit)
                number_host = 2**(bin_mask.count('0'))-2
                number_subnet = 2**(bin_mask.count('1'))
                print(f"Number of subnets \t: {number_subnet} \nNumber of hosts \t: {number_host}")
                hostIP = input_IP + '/' + str(bin_mask.count('1'))
            elif re.fullmatch(r"[0-9]{1,2}",mask_input) and 0<=int(mask_input)<=32:
                hostIP = input_IP + '/' + mask_input
                number_host = 2**(abs(32-int(mask_input)))-2
                number_subnet = 2**(int(mask_input))
                print(f"Number of subnets \t: {number_subnet} \nNumber of hosts \t: {number_host}")
            else:
                print("INVALID SUBNET MASK!!! TRY AGAIN")
                continue
            # following code will find the network address from the given interface address and mask
            print(f"Interface IP \t\t: {input_IP}")
            print("Network Address \t: "+str((ipaddress.ip_interface(hostIP)).network))
            print("Starting Address \t: "+str(ipaddress.ip_interface(hostIP)+1))
            print("Ending Address \t\t: "+str(ipaddress.ip_interface(hostIP)+number_host))
        else:
            app_loop = input("INVALID IP. TRY AGAIN? (y/n)\t:")
            
    else:
        exit()
        app_loop = input("INVALID IP. TRY AGAIN? (y/n)\t:")
        
    app_loop = input("\nEnter new address?(y/n)\t: ")
