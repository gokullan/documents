# Kubernetes

- Set `http_proxy` and `https_proxy` variables in shell if needed
```bash
# proxy-url format: http://username:password@proxy-host:port
export http_proxy='http://proxyServerSddress:proxyPort'    
export https_proxy='https://proxyServerSddress:proxyPort'

# to unset
unset http_proxy
unset https_proxy
```

## `kubectl`
- To list namespaces: `kubectl get namespace`
- To list all pods: `kubectl get pod -n "namespace"` (`-n` is a global option)
- Get pod details: `kubectl get pod -n NAMESPACE -o json POD_NAME`
  - Use `-o jsonpath='{.metadata.labels.tag}'` to get specific values
  - Get container names: `kubectl get pods POD_NAME_HERE -o jsonpath='{.spec.containers[*].name}'`
- To "leave" a cluster: `kubectl config unset current-context`
- To open a remote shell: `kubectl exec -n namespace -it pod_name -c container_name -- /bin/bash`
- Port forwarding: `kubectl port-forward pod local_port:remote_port`

