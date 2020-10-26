# Basic-Wheel
写一些在不同项目中都可能会用到的代码库，同时不同项目在更新对应的代码库时可以汇总到一处。

# Computational Geometry
# Priority-Queue etc.

在不同仓库中，这些文件被频繁使用，在各仓库的迭代过程中，很容易出现更新不同步的情况，造成混乱，因此将这些频繁使用的文件放在一起，每次在各仓库修改时，一定要同时同步这个仓库中的文件。

解决方案是加入了UpdateBasicFiles.py这样的脚本文件，通过比较所有分布式仓库的各个同名文件的修改日期，取最近的修改日期作为替换，批量的对BasicWheel中的代码进行更新。只需右击UpdateBasicFiles，以python运行，即可进行批量更新

更新Heap，template实现 改进Heap的实现，运用了模板，实现算法与数据的分离。