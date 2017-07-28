fid = fopen('data.dat','r');
B = textscan(fid, '%f', 'HeaderLines',2);
B = B{1};
fclose(fid);