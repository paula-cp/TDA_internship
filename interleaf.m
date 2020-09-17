clc;
clear all;
close all;

load('MKL_ASE_1.mat')
F_data_vel=F_data;
load('MKL_ASE_2.mat')
F_data_strains=F_data;  

F_data_vel = F_data_vel';
F_data_strains = F_data_strains';
F_data_final = reshape([F_data_vel(:) F_data_strains(:)]',2*size(F_data_vel,1), [])';

% c = cvpartition(Outcomes,'KFold',5,'Stratify',true);
% 
% train = c.training(2);
% test = c.test(2);
% train_F_data=F_data_final(train,:);
% test_F_data=F_data_final(test,:);
train_out=Outcomes(train,:);
% test_out=Outcomes(test,:);
train_params=ClinParams(train,:);
% test_params=ClinParams(test,:);
%%
load('projected1.mat')
load('projected2.mat')
test_out=Outcomes(test,:);
test_params=ClinParams(test,:);

F_data_vel = projected_test2';
F_data_strains = projected_train';
F_data_final = reshape([F_data_vel(:) F_data_strains(:)]',2*size(F_data_vel,1), [])';
%%
imputed=knnimpute(train_params');
LVMass=imputed(23,:)';
HRecho=imputed(24,:)';
Mitral_EA_ratio=imputed(31,:)';
RWT=imputed(21,:)';
TAPSE=imputed(28,:)';
IVRT=imputed(34,:)';
LVGLS=imputed(38,:)';
data=F_data_final;
Outcomes=train_out;
e=[data,Outcomes,LVMass,HRecho,Mitral_EA_ratio,RWT,TAPSE,IVRT,LVGLS];
for i =1:length(F_data_final)
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
fid = fopen('MKL_train.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('MKL_train.csv',e,'-append');
%% test
imputed=knnimpute(test_params');
LVMass=imputed(23,:)';
HRecho=imputed(24,:)';
Mitral_EA_ratio=imputed(31,:)';
RWT=imputed(21,:)';
TAPSE=imputed(28,:)';
IVRT=imputed(34,:)';
LVGLS=imputed(38,:)';
data=F_data_final;
Outcomes=test_out;
e=[data,Outcomes,LVMass,HRecho,Mitral_EA_ratio,RWT,TAPSE,IVRT,LVGLS];
for i =1:length(F_data_final)
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
fid = fopen('MKL_test.csv','w'); 
fprintf(fid,'%s\n',textHeader)
fclose(fid)
%write data to end of file
dlmwrite('MKL_test.csv',e,'-append');
