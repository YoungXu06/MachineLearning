#### k近邻的实现：kd树

实现k近邻算法时，主要考虑的问题是如何对数据进行快速的k近邻搜索。

为了提高k近邻搜索的效率，可以考虑使用特殊的结构存储训练数据，以减少计算距离的次数。

- **构造kd树**

*构造平衡kd树*

输入：K维空间数据集 $T={x_{1}, x_{2},...,x_{N}}$

其中$x_{i}=(x_{i}^{(1)}, x_{i}^{(2)}, ..., x_{i}^{(k)})$

输出：kd树

（1）开始：构造根节点，根节点对应于包含 $T$ 的 $k$ 维空间的超矩形区域。

​    选择 $x^{(1)}$ 为坐标轴，以 $T$ 中所有实例 $x^{(1)}$ 的中位数为切分点，将根节点对应的超矩形区域分成两个子区域。切分由通过切分点，且与坐标轴 $x^{(1)}$ 垂直的超平面实现。

​    由根节点生成深度为1的左、右节点：左子节点对应坐标 $x^{(1)}$ 小于切分点，右子节点大于切分点。

​    将落在切分超平面上的实例保存在根节点。

（2）重复：将深度为 $j$ 的节点，选择 $x^{(l)}$ 为切分的坐标轴，$l=j(mod k)+1$ ，同（1）的操作。

（3）直到两个子区域没有实例存在时停止，从而形成kd树的区域划分。

- **搜索kd树**

*用kd树的最近邻搜索*

输入：已构造的kd树；目标点x

输出：x的最近邻

（1）在kd树中找包含目标点x的叶节点：从根节点出发，递归地向下访问kd树。若目标点x当前维的坐标小于切分点的坐标则移动到左子节点，反之移动到右子节点。直到节点为叶子节点为止。

（2）以此叶节点为“当前最近点”

（3）递归向上回退，在每个节点进行如下操作：

> - 如果该节点保存的实例点比当前最接近点距离目标点更近，则以该实例点为“当前最近点”
> - 当前最近点一定存在于该节点的一个子节点对应的区域。检查该子节点的父节点的另一子节点对应的区域是否有更近的点。具体地，检查另一子节点对应的区域是否与以目标点为球心、以目标点与“当前最近点”间的距离为半径的超球体相交。
> - 如果相交，可能在另一个子节点对应的区域内存在距目标更近的点，移动到另一个子节点。接着，递归地进行最近邻搜索。

（4）当回退到根节点时，搜索结束。最后的“当前最近点”即为x的最近邻点

------

**如果实例点是随机分布的，kd树搜索的平均计算复杂度是$O(logN)$ ，N为训练实例数。kd数更适用于训练实例数远大于空间维数时的k近邻搜索。当空间维数接近训练实例数时，它的效率会迅速下降，几乎接近线性扫描。**

------

