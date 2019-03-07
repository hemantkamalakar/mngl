import requests
from bs4 import BeautifulSoup
import json

class MNGL(object):
    """ Class to get MNGL bill """
    def __init__(self, bp_no):
        """ __init__ """
        self.serverurl = 'https://www.mngl.in/onlinebill/payment/ajax_load_bp_info'
        self.bp_no = bp_no

    def get_bill_details(self):
        billdetails = {}
        data = {}
        url = self.serverurl 
        data = { 'bp_no': self.bp_no }
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        try :
            response = requests.post(url,headers=headers, data=data,timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text,"lxml")
             
                billdetails['customer_name'] = soup.find('input', {'name': 'customer_name'}).get('value')
                billdetails['customer_id']  = soup.find('input', {'name': 'customer_id'}).get('value')
                billdetails['email'] = soup.find('input', {'id': 'email'}).get('value')
                billdetails['mobile'] = soup.find('input', {'id': 'mobile'}).get('value')
                billdetails['billno'] = soup.find('input', {'name': 'bill_no'}).get('value')
                billdetails['amount'] = soup.find('input', {'id': 'amount'}).get('value')
                billdetails['billdate'] = soup.find_all("label", string="Bill Date. :")[0].find_next_sibling().get('value')
                billdetails['billduedate']  = soup.find_all("label", string="Bill Due Date. :")[0].find_next_sibling().get('value')
                return json.dumps(billdetails)
            else:
                return {}    
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")



def main():
    mngl = MNGL(bp_no=123456)
    billdetails = mngl.get_bill_details()
    print(billdetails)

if __name__ == "__main__":
    main()
