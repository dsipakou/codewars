class Solution:
    def validIPAddress(self, IP: str) -> str:
        parsed_ip = IP.split('.')
        if len(parsed_ip) == 4:
            if self.validate_ipv4(parsed_ip):
                return "IPv4"
            else:
                return "Neither"
        parsed_ip = IP.split(':')    
        if len(parsed_ip) == 8:
            if self.validate_ipv6(parsed_ip):
                return "IPv6"
        
        return "Neither"
        
        
    def validate_ipv4(self, ip):
        for segment in ip:
            try:
                if len(segment) == len(str(int(segment))) and int(segment) < 256 and int(segment) >= 0:
                    continue
                else:
                    return False
            except ValueError:
                return False
        return True
    
    def validate_ipv6(self, ip):
        for segment in ip:
            try:
                if len(segment) > 0 and len(segment) <= 4 and int(segment, base=16) >= 0 and segment.isalnum():
                    continue
                else:
                    return False
            except ValueError:
                return False
        return True
