library(netmeta)
data <- read.csv("data.csv", header = T,sep = ",")
head(data)
#2. 效应转换及模型构
net <- pairwise(treat = treatment,
                n= sampleSize, 
                mean = mean,
                sd = std.dev, 
                data = data, 
                studlab = study,               
                sm = "MD")
m.netmeta <- netmeta(net ,
                     fixed = TRUE,
                     random = FALSE)
summary(m.netmeta)