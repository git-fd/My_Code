#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <functional>
using namespace std;
struct TreeNode // 节点结构定义
{
    int val;         // 值
    TreeNode *left;  // 左孩子
    TreeNode *right; // 右孩子
    // 构造函数
    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
    TreeNode(int val, TreeNode *left, TreeNode *right) : val(val), left(left), right(right) {}
};
struct Tree // 二叉树的相关操作
{

    static void run()
    {
        int op = 0; // 操作数定义
        do
        {
            // 菜单显示
            cout << endl;
            cout << "       二叉树后序非递归遍历系统       " << endl;
            cout << "----------   1.系统测试    ----------" << endl;
            cout << "----------   2.自定义测试  ----------" << endl;
            cout << "----------   0.退出系统    ----------" << endl;
            cout << "请输入您的选择：";
            cin >> op;
            // 操作
            switch (op)
            {
            case 1:
                Tree::print(Tree::create(vector<int>{3, 9, 20, 15, 7}, vector<int>{9, 3, 15, 20, 7}));
                break;
            case 2:
                int t;
                cout << "请选择建树方式（1.先序递归建树，2.前序中序序列建树）：";
                cin >> t;
                if (t == 1)
                {
                    cout << "按照先序递归输入二叉树（#表示结点为空）：";
                    Tree::print(Tree::create());
                }
                else
                {
                    int n;
                    cout << "请输入结点个数：";
                    cin >> n;
                    vector<int> pre(n), in(n);
                    cout << "请输入先序遍历：";
                    for (auto &x : pre)
                        cin >> x;
                    cout << "请输入中序遍历：";
                    for (auto &x : in)
                        cin >> x;
                    Tree::print(Tree::create(pre, in));
                }
                break;
            }
        } while (op);
    }

    static vector<int> postorder(TreeNode *root) // 后序非递归遍历
    {
        vector<int> res;            // 定义结果保存数组
        stack<TreeNode *> st;       // 定义辅助栈
        TreeNode *p = nullptr;      // 标志指针
        while (root || !st.empty()) // 当节点不为空或者栈不为空进入循环
        {
            while (root) // 将左子树全部入栈
            {
                st.push(root);
                root = root->left;
            }
            root = st.top(); // 取栈顶元素

            if (!root->right || root->right == p) // 判断栈顶元素是否存在右孩子或栈顶来自左子树
            {
                st.pop();                 // 出栈
                res.push_back(root->val); // 对节点操作
                p = root;                 // 标志
                root = nullptr;
            }
            else
                root = root->right; // 移向右子树
        }
        return res; // 返回结果数组
    }
    static TreeNode *create() // 先序递归建立二叉树
    {
        string val;
        cin >> val;
        if (val == "#")
            return nullptr; // 为#返回空

        return new TreeNode(stoi(val), create(), create()); // 递归过程并返回
    }
    static TreeNode *create(vector<int> pre, vector<int> in) // 先序中序序列递归建立二叉树
    {
        unordered_map<int, int> pos;
        for (int i{}; auto x : in) // 哈希建立
            pos[x] = i++;
        function<TreeNode *(int, int, int, int)> helper = [&](int pl, int pr, int il, int ir) -> TreeNode * // 辅助递归函数
        {
            if (pl > pr)
                return nullptr;                                                                                           // 递归出口
            int k = pos[pre[pl]] - il;                                                                                    // 当前处理的点
            return new TreeNode(pre[pl], helper(pl + 1, pl + k, il, il + k - 1), helper(pl + k + 1, pr, il + k + 1, ir)); // 递归过程并返回
        };
        return helper(0, pre.size() - 1, 0, in.size() - 1); // 返回结果
    }
    static void print(TreeNode *root) // 结果显示
    {
        cout << "树形结构：" << endl;
        printTree(root); // 树形显示
        cout << "后序遍历为：";
        for (auto x : postorder(root)) // 后序遍历序列
            cout << x << ' ';
        cout << endl;
    }

private:
    static void printTree(TreeNode *root)
    {
        if (!root)
            return;
        auto tmp = root;
        vector<TreeNode *> intv = inorder(tmp); // 中序遍历节点数组
        string template_str;                    // 模板string，表示每行打印string的长度
        int location = 0;
        unordered_map<TreeNode *, int> first_locations; // 存储节点对应在本行string中的首位置
        for (auto &i : intv)
        {
            location = template_str.size();
            template_str += to_string(i->val) + " ";
            first_locations[i] = location;
        }
        for (auto &i : template_str)
            i = ' '; // 把模板全部置为空格方便后续使用
        // 层序遍历
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            int currentLevelSize = q.size();
            int cur_loc = 0;
            string tmp_str1 = template_str, tmp_str2 = template_str; // 1为节点所在行，2为其下一行
            for (int i = 1; i <= currentLevelSize; ++i)
            {
                auto node = q.front();
                q.pop();
                cur_loc = first_locations[node];
                string num_str = to_string(node->val);

                // 左边，如果存在左孩子，那么在第二行对应位置打印'/'，在第一行补上'_'
                if (node->left)
                {
                    q.push(node->left);
                    int first_loc = first_locations[node->left] + 1;
                    tmp_str2[first_loc++] = '/';
                    while (first_loc < cur_loc)
                        tmp_str1[first_loc++] = '_';
                }

                // 中间,对应位置打印节点值（有可能为多位数）
                for (int j = 0; j < num_str.length(); ++j, ++cur_loc)
                    tmp_str1[cur_loc] = num_str[j];

                // 右边，如果存在右孩子，那么在第二行对应位置打印'\'，在第一行补上'_'
                if (node->right)
                {
                    q.push(node->right);
                    int last_loc = first_locations[node->right] - 1;
                    tmp_str2[last_loc] = '\\';
                    while (cur_loc < last_loc)
                        tmp_str1[cur_loc++] = '_';
                }
            }

            // 打印两行
            cout << tmp_str1 << endl;
            cout << tmp_str2 << endl;
        }
    }
    static vector<TreeNode *> inorder(TreeNode *root) // 辅助中序遍历存储节点指针
    {
        vector<TreeNode *> res;
        stack<TreeNode *> stk;
        while (root != nullptr || !stk.empty())
        {
            while (root != nullptr)
            {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            res.push_back(root);
            root = root->right;
        }
        return res;
    }
};