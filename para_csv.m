name=1:100;
e=[name;curves;label]';
for i =0:3250
    cHeader{i+1}=mat2str(i);
end
cHeader{i+2}='out';
%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('vaya_cora.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('vaya_cora.csv',e,'-append');
%%
% sp=zeros(150,1);
% for i = 1:150
%     if species{i}=="setosa"
%         sp(i)=0;
%     elseif species{i}=="versicolor"
%         sp(i)=1;
%     else
%         sp(i)=2;
%     end
% end
% e=[meas,sp];
% 
% cHeader{1}='sepal l';
% cHeader{2}='sepal w';
% cHeader{3}='petal l';
% cHeader{4}='petal w';
% cHeader{5}='species';
% 
% %cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
% commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
% commaHeader = commaHeader(:)';
% textHeader = cell2mat(commaHeader); %cHeader in text with commas
% %write header to file
% fid = fopen('vaya.csv','w'); 
% fprintf(fid,'%s\n',textHeader)
% fclose(fid)
% %write data to end of file
% dlmwrite('vaya.csv',e,'-append');

%% A
name=1:99;
e=A;
for i =1:99
    cHeader{i}=mat2str(i);
end
%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('vaya_dim.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('vaya_dim.csv',e,'-append');

%% Betas
e=betas;

cHeader{1}=mat2str(1);
%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('vaya_beta.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('vaya_beta.csv',e,'-append');

%% new data
imputed=knnimpute(ClinParams');
LVMass=imputed(27,:)';
HRecho=imputed(28,:)';
Mitral_EA_ratio=imputed(35,:)';
RWT=imputed(25,:)';
TAPSE=imputed(32,:)';
IVRT=imputed(38,:)';
LVGLS=imputed(43,:)';
data=F_data(:,1:3);
e=[data,Outcomes,LVMass,HRecho,Mitral_EA_ratio,RWT,TAPSE,IVRT,LVGLS];
for i =1:3
    cHeader{i}=mat2str(i);
end
cHeader{i+1}='out';
cHeader{i+2}='LV';
cHeader{i+3}='echo';
cHeader{i+4}='mitral';
cHeader{i+5}='RWT';
cHeader{i+6}='TAPSE';
cHeader{i+7}='IVRT';
cHeader{i+8}='LVGLS';

%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('MKL2_fixed.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('MKL2_fixed.csv',e,'-append');

%% new data clinparams
e=[ClinParams(:,1:41),Outcomes];
for i =1:41
    cHeader{i}=mat2str(i);
end
cHeader{i+1}='out';
%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('MDS_full.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('MDS_full.csv',e,'-append');

%% super new approach
imputed=knnimpute(ClinParams');
LVMass=imputed(27,:)';
HRecho=imputed(28,:)';
Mitral_EA_ratio=imputed(35,:)';
RWT=imputed(25,:)';
TAPSE=imputed(32,:)';
IVRT=imputed(38,:)';
LVGLS=imputed(43,:)';
e=[F_data,Outcomes,LVMass,HRecho,Mitral_EA_ratio,RWT,TAPSE,IVRT,LVGLS];
for i =1:283
    cHeader{i}=mat2str(i);
end
cHeader{i+1}='out';
cHeader{i+2}='LV';
cHeader{i+3}='echo';
cHeader{i+4}='mitral';
cHeader{i+5}='RWT';
cHeader{i+6}='TAPSE';
cHeader{i+7}='IVRT';
cHeader{i+8}='LVGLS';

%cHeader = {'ab' 'bcd' 'cdef' 'dav'}; %dummy header
commaHeader = [cHeader;repmat({','},1,numel(cHeader))]; %insert commaas
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas
%write header to file
fid = fopen('MKL2_MDS.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('MKL2_MDS.csv',e,'-append');