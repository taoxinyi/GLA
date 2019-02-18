SET date=%1
SET filename1=files_detail_%date%.csv
SET filename2=methods_detail_%date%.csv
ren files_detail.csv %filename1%
ren methods_detail.csv %filename2%
pscp.exe -l intel -pw intel %filename1% intel@10.239.140.245:/home/intel/test
pscp.exe -l intel -pw intel %filename2% intel@10.239.140.245:/home/intel/test