redef some_regex = /www\.google\.com/ 
  | /1\.2\.3\.4/ 
    ;

event bro_init()
{
    local a = 1.2;
    local b = 1.2.3.4;
    local c = www.google.com;
    local d = "www.google.com";
}
