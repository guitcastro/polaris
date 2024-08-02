/*
 * Copyright (c) 2024 Snowflake Computing Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.polaris.service.catalog;

import io.polaris.core.storage.PolarisStorageActions;
import java.util.Map;
import java.util.Set;
import org.apache.iceberg.TableMetadata;
import org.apache.iceberg.catalog.TableIdentifier;

/**
 * Adds support for credential vending for (typically) {@link org.apache.iceberg.TableOperations} to
 * fetch access credentials that are inserted into the {@link
 * org.apache.iceberg.rest.responses.LoadTableResponse#config()} property. See the
 * rest-catalog-open-api.yaml spec for details on the expected format of vended credential
 * configuration.
 */
public interface SupportsCredentialDelegation {
  Map<String, String> getCredentialConfig(
      TableIdentifier tableIdentifier,
      TableMetadata tableMetadata,
      Set<PolarisStorageActions> storageActions);
}
