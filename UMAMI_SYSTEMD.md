# Umami on Minerva with systemd

This runbook assumes the Umami stack from `docker-compose.umami.yml` is copied to Minerva and managed by systemd.

## 1. Install Docker

Install Docker Engine and the Compose plugin on Minerva, then confirm these commands work:

```bash
docker --version
docker compose version
```

## 2. Put the repo on Minerva

Clone or copy this repository to a fixed path, for example:

```bash
/opt/palabrasalviento
```

The compose file should stay in that directory.

Create a `.env` file next to `docker-compose.umami.yml` based on `.env.example` and put real secrets there. Compose will read it automatically from the project directory.

Recommended minimum values:

```bash
UMAMI_DB_PASSWORD=$(openssl rand -base64 24)
UMAMI_APP_SECRET=$(openssl rand -base64 48)
```

## 3. Create the systemd unit

Create `/etc/systemd/system/umami.service` with this content:

```ini
[Unit]
Description=Umami analytics stack
Requires=docker.service
After=docker.service network-online.target
Wants=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/palabrasalviento
ExecStart=/usr/bin/docker compose -f docker-compose.umami.yml up -d
ExecStop=/usr/bin/docker compose -f docker-compose.umami.yml down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

If Docker is installed in a different path, update `/usr/bin/docker` to the output of `which docker`.

## 4. Enable and start it

Run:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now umami
sudo systemctl status umami
```

If you want the dashboard reachable from the tailnet and from the new blog tab, make sure Docker publishes port 3000 on all interfaces instead of only on `127.0.0.1`.

If you are placing Umami behind a reverse proxy or Tailscale Serve, keep the app private on localhost and expose only the proxy.

## 5. Verify the app

Check the service logs and the web port:

```bash
docker compose -f /opt/palabrasalviento/docker-compose.umami.yml ps
curl -I http://127.0.0.1:3000
```

For a healthier check, inspect the container health status too:

```bash
docker compose -f /opt/palabrasalviento/docker-compose.umami.yml ps --format json
```

If the database is still starting, wait for `healthy` before troubleshooting the Umami container.

## 6. Reach it from your tailnet

If you want to keep Umami private on Minerva, leave the compose port bound to `127.0.0.1:3000` and expose it through Tailscale Serve or an SSH tunnel.

If the blog itself is public, the Umami script URL must be reachable by visitors. In that case, point `umami_src` in `_config.yml` at a publicly reachable HTTPS URL instead of a tailnet-only address.

If you want the Umami tab in the blog navigation to open directly, the dashboard must be reachable at `http://100.64.0.43:3000` or another public URL.

## 7. Update the blog config

Once Minerva has a reachable URL, change `umami_src` in `_config.yml` to that URL and keep the `umami_website_id` value created in Umami.

## 8. Make the embed actually work

If you want the Umami page in the blog to embed instead of falling back to a link, expose the dashboard over HTTPS with Tailscale Serve and then copy that HTTPS URL into `umami_embed_url` in `_config.yml`.

Typical flow on Minerva:

```bash
tailscale serve --bg localhost:3000
tailscale serve status
```

Use the HTTPS URL shown by `tailscale serve status` as `umami_embed_url`.

If you later want to remove the proxy:

```bash
tailscale serve off
```

If the dashboard is only on plain HTTP, the browser will keep blocking the iframe from the HTTPS blog page.
