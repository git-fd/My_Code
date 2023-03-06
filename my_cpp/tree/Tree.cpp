#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
    TreeNode(int val, TreeNode *left, TreeNode *right) : val(val), left(left), right(right) {}
};

struct Tree
{
    static vector<int> postorder(TreeNode *root)
    {
        vector<int> res;
        stack<TreeNode *> st;
        TreeNode *p = nullptr;
        while (root || !st.empty())
        {
            while (root)
            {
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            if (!root->right || root->right == p)
            {
                res.push_back(root->val);
                p = root;
                root = nullptr;
            }
            else
            {
                st.push(root);
                root = root->right;
            }
        }
        return res;
    }

    static void printTree(TreeNode *root)
    {
        if (!root) return;
        auto tmp = root;
        vector<TreeNode *> intv = inorder(tmp); // 中序遍历节点数组
        string template_str;                             // 模板string，表示每行打印string的长度
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
                {
                    tmp_str1[cur_loc] = num_str[j];
                }
                // 右边，如果存在右孩子，那么在第二行对应位置打印'\'，在第一行补上'_'
                if (node->right)
                {
                    q.push(node->right);
                    int last_loc = first_locations[node->right] - 1;
                    tmp_str2[last_loc] = '\\';
                    while (cur_loc < last_loc)
                    {
                        tmp_str1[cur_loc++] = '_';
                    }
                }
            }
            // 打印两行
            cout << tmp_str1 << endl;
            cout << tmp_str2 << endl;
        }
    }

private:
    static vector<TreeNode *> inorder(TreeNode *root)
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

int test()
{
    TreeNode *root = new TreeNode(1, new TreeNode(0), new TreeNode(2));

    Tree::printTree(root);

    return 0;
}