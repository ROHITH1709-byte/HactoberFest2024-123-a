#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define nl '\n'
const ll maxn = 2e5 + 20;
const ll LOG = 20; // Because 2^20 > 1e5
vector<ll> adj[maxn];
ll up[maxn][LOG]; // up[v][j] is the 2^j-th ancestor of v
ll depth[maxn];

// DFS to initialize up table and depth array
void dfs(ll v, ll p) {
    up[v][0] = p; // The 2^0-th ancestor (parent)
    for (ll i = 1; i < LOG; i++) {
        if (up[v][i - 1] != -1) {
            up[v][i] = up[up[v][i - 1]][i - 1]; // Set the 2^i-th ancestor
        } else {
            up[v][i] = -1; // No ancestor
        }
    }
    for (auto u : adj[v]) {
        if (u != p) {
            depth[u] = depth[v] + 1; // Set depth for child nodes
            dfs(u, v);
        }
    }
}

// Function to find LCA of u and v
ll lca(ll u, ll v) {
    if (depth[u] < depth[v]) {
        swap(u, v); // Ensure u is the deeper node
    }

    // Lift u up until it's the same depth as v
    ll diff = depth[u] - depth[v];
    for (ll i = 0; i < LOG; i++) {
        if ((diff >> i) & 1) { // If the i-th bit of diff is set, lift u by 2^i
            u = up[u][i];
        }
    }

    if (u == v) return u; // If u and v are the same, return u

    // Now lift both u and v until their lowest common ancestor is found
    for (ll i = LOG - 1; i >= 0; i--) {
        if (up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }

    return up[u][0]; // The parent of u (or v) is the LCA
}

void run() {
    ll n, q;
    cin >> n >> q;

    // Read edges and construct the tree
    for (ll i = 1; i < n; i++) { // Loop from 1 to n-1 for n-1 edges
        ll u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    memset(up, -1, sizeof(up));
    depth[1] = 0; // Initialize depth of root
    dfs(1, -1); // Start DFS from root node (1)

    while (q--) {
        ll u, v;
        cin >> u >> v;
        ll lcaNode = lca(u, v);
        ll ans = depth[u] + depth[v] - 2 * depth[lcaNode]; // Distance calculation
        cout << ans << nl;
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    run();
    return 0;
}
