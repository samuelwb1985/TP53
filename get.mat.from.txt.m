

%%filename='1.MMR12m.NO.specific.matrix'

fid = fopen(filename,'rt');  %# Open the data file

data = textscan(fid, '%s' ,1 ,'Delimiter', '\n'  );
cancerType =  data{1,1}{1}; 
 
data = textscan(fid, '%s' ,1 ,'Delimiter', '\n'  );
first = textscan(data{1,1}{1}, '%s' ,'Delimiter', '\t'  );
types=first{1,1};

data = textscan(fid, '%s' ,1 ,'Delimiter', '\n'  );
second = textscan(data{1,1}{1}, '%s' ,'Delimiter', '\t'  );
subtypes=second{1,1};

data = textscan(fid, '%s' ,1 ,'Delimiter', '\n'); %, 'bufsize', 65520);
third = textscan(data{1,1}{1}, '%s', 'Delimiter', '\t');
sampleNames=third{1,1};

fclose(fid);

Data=importdata(filename);
originalGenomes=Data.data;

[Row Lol]=size(originalGenomes);

[Row1 Lol1]=size(sampleNames);
if Lol ~= Row1
   error('ERROR sampleNames row number wrong ')   
end
if Lol1 ~= 1
   error('ERROR sampleNames col number wrong ')   
end

[Row1 Lol1]=size(subtypes);
if Row ~= Row1
   error('ERROR subtypes row number wrong ')   
end
if Lol1 ~= 1
   error('ERROR subtypes col number wrong ')   
end

[Row1 Lol1]=size(types);
if Row ~= Row1
   error('ERROR types row number wrong ')   
end
if Lol1 ~= 1
   error('ERROR types col number wrong ')   
end
		
size(originalGenomes)
size(sampleNames)
size(subtypes)
size(types)
save( strrep(filename,'.txt','.mat'),'cancerType','originalGenomes','sampleNames','subtypes','types')














